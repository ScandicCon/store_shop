from typing import Optional
from pydantic import BaseModel

class CreateProduct(BaseModel):
    name: str
    category: str
    size: str
    color: str
    price: int
    description: str
    image_url: Optional[str] = None

class ProductRead(BaseModel):
    id: int
    name: str
    category: str
    size: str
    color: str
    price: int
    description: str
    image_url: Optional[str] = None