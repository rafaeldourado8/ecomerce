from . import models
from . import schema 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def create_new_product(request: schema.Product, database: AsyncSession) -> models.Product:
    new_product = models.Product(
        name=request.name,
        qtd=request.qtd, 
        description=request.description,
        price=request.price,
        category_id=request.category_id
    )
    
    database.add(new_product)
    await database.commit()
    await database.refresh(new_product)
    return new_product

async def list_all_products(database: AsyncSession) -> list[models.Product]:
    query = select(models.Product)
    result = await database.execute(query)
    products = result.scalars().all()
    return products

async def get_product_by_id(product_id: int, database: AsyncSession) -> models.Product:
    query = select(models.Product).where(models.Product.id == product_id)
    result = await database.execute(query)
    product = result.scalars().first()
    return product

async def delete_product(product_id: int, database: AsyncSession) -> None:
    product = await get_product_by_id(product_id, database)
    await database.delete(product)
    await database.commit()

async def update_product(product_id: int, request: schema.UpdateProduct, database: AsyncSession) -> models.Product:
    product = await get_product_by_id(product_id, database)
    
    product.name = request.name
    product.qtd = request.qtd
    product.description = request.description
    product.price = request.price
    product.category_id = request.category_id
    
    await database.commit()
    await database.refresh(product)
    return product


async def create_new_category(request: schema.Category, database: AsyncSession) -> models.Category:
    new_category = models.Category(name=request.name)
    
    database.add(new_category)
    await database.commit()
    await database.refresh(new_category)
    return new_category

async def list_all_categories(database: AsyncSession) -> list[models.Category]:
    query = select(models.Category)
    result = await database.execute(query)
    categories = result.scalars().all()
    return categories

async def get_category_by_id(category_id: int, database: AsyncSession) -> models.Category:
    query = select(models.Category).where(models.Category.id == category_id)
    result = await database.execute(query)
    category = result.scalars().first()
    return category

async def delete_category(category_id: int, database: AsyncSession) -> None:
    category = await get_category_by_id(category_id, database)
    await database.delete(category)
    await database.commit()

async def update_category(category_id: int, request: schema.Category, database: AsyncSession) -> models.Category:
    category = await get_category_by_id(category_id, database)
    
    category.name = request.name
    
    await database.commit()
    await database.refresh(category)
    return category