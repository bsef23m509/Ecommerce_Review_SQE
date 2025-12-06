from pydantic import BaseModel
from typing import List

class Review(BaseModel):
    text: str
    rating: int

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str
    reviews: List[Review] = []
