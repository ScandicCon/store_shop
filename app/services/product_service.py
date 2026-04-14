from sqlmodel import Session, select
from app.db.models import Product

def create_product(session: Session, product_data: dict):
    new_product = Product(**product_data)
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product

def get_all_products(session: Session):
    return session.exec(select(Product)).all()

def get_product_by_id(session: Session, product_id: int):
    return session.exec(select(Product).where(Product.id == product_id)).first()