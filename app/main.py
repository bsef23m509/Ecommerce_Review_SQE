from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="E-commerce Review Demo")
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# In-memory fake database
products = [
    {"id": 1, "name": "Laptop", "description": "A fast laptop", "reviews": []},
    {"id": 2, "name": "Headphones", "description": "Noise-cancelling", "reviews": []},
    {"id": 3, "name": "Smartphone", "description": "Android device", "reviews": []},
]

def get_product(pid: int):
    for p in products:
        if p["id"] == pid:
            return p
    return None

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'products': products})

@app.get('/product/{product_id}', response_class=HTMLResponse)
def product_page(request: Request, product_id: int):
    p = get_product(product_id)
    if not p:
        raise HTTPException(status_code=404, detail='Product not found')
    return templates.TemplateResponse('product.html', {'request': request, 'product': p})

@app.post('/product/{product_id}/reviews')
def add_review(product_id: int, review: str = Form(...)):
    if not review or len(review.strip()) < 3:
        return {'error': 'Review too short'}
    p = get_product(product_id)
    if not p:
        raise HTTPException(status_code=404, detail='Product not found')
    p['reviews'].append({'text': review.strip()})
    return RedirectResponse(url=f'/product/{product_id}', status_code=303)

# Simple JSON API
@app.get('/api/products')
def api_products():
    return products

@app.get('/api/products/{product_id}')
def api_product(product_id: int):
    p = get_product(product_id)
    if not p:
        raise HTTPException(status_code=404, detail='Product not found')
    return p
