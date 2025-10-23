from . import models
from . import schema 
from sqlalchemy.orm import Session

async def create_new_product(request: schema.Product, database: Session) -> models.Product:
    new_product = models.Product(
        name=request.name,
        qtd=request.qtd, 
        description=request.description,
        price=request.price,
        category_id=request.category_id
    )
    
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product

async def list_all_products(database: Session) -> list[models.Product]:
    products = database.query(models.Product).all()
    return products

async def get_product_by_id(product_id: int, database: Session) -> models.Product:
    product = database.query(models.Product).filter(models.Product.id == product_id).first() 
    return product

async def delete_product(product_id: int, database: Session) -> None:
    product = await get_product_by_id(product_id, database)
    database.delete(product)
    database.commit()

async def update_product(product_id: int, request: schema.UpdateProduct, database: Session) -> models.Product:
    product = await get_product_by_id(product_id, database)
    
    product.name = request.name
    product.qtd = request.qtd
    product.description = request.description
    product.price = request.price
    product.category_id = request.category_id
    
    database.commit()
    database.refresh(product)
    return product


async def create_new_category(request: schema.Category, database: Session) -> models.Category:
    new_category = models.Category(name=request.name)
    
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category

async def list_all_categories(database: Session) -> list[models.Category]:
    categories = database.query(models.Category).all()
    return categories

async def get_category_by_id(category_id: int, database: Session) -> models.Category:
    category = database.query(models.Category).filter(models.Category.id == category_id).first()
    return category

async def delete_category(category_id: int, database: Session) -> None:
    category = await get_category_by_id(category_id, database)
    database.delete(category)
    database.commit()

async def update_category(category_id: int, request: schema.Category, database: Session) -> models.Category:
    category = await get_category_by_id(category_id, database)
    
    category.name = request.name
    
    database.commit()
    database.refresh(category)
    return category