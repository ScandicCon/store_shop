from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.db.database import get_session
from app.schemas.product import CreateProduct
from app.services.product_service import create_product as create_product_service
from app.services.product_service import get_all_products, get_product_by_id

router = APIRouter(tags=["products"])

@router.post("/product/append")
def create_product(
    product: CreateProduct,
    session: Session = Depends(get_session),
):
    return create_product_service(session, product.model_dump())

@router.get("/all/products")
def get_all(session: Session = Depends(get_session)):
    return get_all_products(session)

@router.get("/product/{id}")
def get_product(id: int, session: Session = Depends(get_session)):
    product = get_product_by_id(session, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product