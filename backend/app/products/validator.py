from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional

from . models import Product, Category 

async def verify_product_exist(product_name: str, db_session: AsyncSession) -> Optional[Product]:
    query = select(Product).where(Product.name == product_name)
    result = await db_session.execute(query)
    return result.scalars().first()

async def verify_product_id_exist(product_id: int, db_session: AsyncSession) -> Optional[Product]:
    query = select(Product).where(Product.id == product_id)
    result = await db_session.execute(query)
    return result.scalars().first()

async def verify_category_id_exist(category_id: int, db_session: AsyncSession) -> bool:
    query = select(Category).where(Category.id == category_id)
    result = await db_session.execute(query)
    category = result.scalars().first()
    return category is not None

async def verify_category_name_exist(category_name: str, db_session: AsyncSession) -> Optional[Category]:
    '''Verifica se uma categoria já existe pelo nome'''
    query = select(Category).where(Category.name == category_name)
    result = await db_session.execute(query)
    return result.scalars().first()

async def verify_category_has_products(category_id: int, db_session: AsyncSession) -> bool:
    '''Verifica se uma categoria possui produtos associados'''
    query = select(Product).where(Product.category_id == category_id)
    result = await db_session.execute(query)
    product = result.scalars().first()
    return product is not None