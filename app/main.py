import json
import threading
from pathlib import Path
from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from app.models import Product

PRODUCTS_FILE_PATH = Path("products.json")
LOCK = threading.Lock()

app = FastAPI(title="E-commerce Product Review API")
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# JSON file helpers
def load_products():
    with LOCK:
        if not PRODUCTS_FILE_PATH.exists():
            raise FileNotFoundError("products.json not found")
        with open(PRODUCTS_FILE_PATH, "r") as f:
            return json.load(f)


def save_products(products):
    with LOCK:
        with open(PRODUCTS_FILE_PATH, "w") as f:
            json.dump(products, f, indent=2)


# In-memory cache loaded at startup
products = load_products()


def get_product(pid: int):
    for p in products:
        if p["id"] == pid:
            return p
    return None


# Web Pages
@app.get("/", response_class=HTMLResponse, tags=["Web Pages"])
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "products": products}
    )


@app.get("/product/{product_id}", response_class=HTMLResponse, tags=["Web Pages"])
def product_page(request: Request, product_id: int):
    p = get_product(product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")

    return templates.TemplateResponse(
        "product.html",
        {"request": request, "product": p}
    )


@app.post("/product/{product_id}/reviews", tags=["Apis"])
def add_review(
    product_id: int,
    review: str = Form(None, description="Text of the review"),
    rating: int = Form(None, description="Rating between 1 and 5")
):

    if review is None:
        raise HTTPException(status_code=400, detail="Review text missing or empty")

    if rating is None:
        raise HTTPException(status_code=400, detail="Review rating missing")

    if rating < 1 or rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")


    p = get_product(product_id)

    if not p:
        raise HTTPException(status_code=404, detail="Product not found")

    # Add review
    p["reviews"].append({
        "text": review.strip(),
        "rating": rating
    })

    # Save back to DB
    save_products(products)

    return RedirectResponse(url=f"/product/{product_id}", status_code=303)


# JSON API
@app.get("/api/products", response_model=List[Product], tags=["Apis"])
def api_products():
    return products


@app.get("/api/products/{product_id}", response_model=Product, tags=["Apis"])
def api_product(product_id: int):
    p = get_product(product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return p
