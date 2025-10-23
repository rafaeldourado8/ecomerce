from sqlalchemy.orm import Session
from typing import Optional

from . models import Product, Category 

def verify_product_exist(product_name: str, db_session: Session) -> Optional[Product]:
    return db_session.query(Product).filter(Product.name == product_name).first()

def verify_product_id_exist(product_id: int, db_session: Session) -> Optional[Product]:
    return db_session.query(Product).filter(Product.id == product_id).first()

def verify_category_id_exist(category_id: int, db_session: Session) -> bool:
    category = db_session.query(Category).filter(Category.id == category_id).first()
    return category is not None

def verify_category_name_exist(category_name: str, db_session: Session) -> Optional[Category]:
    '''Verifica se uma categoria já existe pelo nome'''
    return db_session.query(Category).filter(Category.name == category_name).first()