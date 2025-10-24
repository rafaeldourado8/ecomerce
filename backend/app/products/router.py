from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from app import db
from . import services
from . import schema
from . import validator

products_router = APIRouter(tags=['Products'], prefix='/products')

@products_router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.ShowProduct)
async def create_product(request: schema.Product, database: AsyncSession = Depends(db.get_db)):
    '''Funcao para criar um novo produto'''
    
    if not await validator.verify_category_id_exist(request.category_id, database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com id {request.category_id} não encontrada."
        )

    if await validator.verify_product_exist(request.name, database):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Produto com o nome '{request.name}' já existe."
        )

    new_product = await services.create_new_product(request, database)
    return new_product


@products_router.get('/', response_model=List[schema.ShowProduct], status_code=status.HTTP_200_OK)
async def get_all_products(database: AsyncSession = Depends(db.get_db)):
    '''Funcao para obter todos os produtos'''
    products = await services.list_all_products(database)
    return products


@products_router.get('/{product_id}', response_model=schema.ShowProduct, status_code=status.HTTP_200_OK)
async def get_product_by_id(product_id: int, database: AsyncSession = Depends(db.get_db
)):
    '''Funcao para obter um produto pelo ID'''
    product = await services.get_product_by_id(product_id, database)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Produto com id {product_id} não encontrado."
        )
    return product


@products_router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_by_id(product_id: int, database: AsyncSession = Depends(db.get_db
)):
    '''Funcao para deletar um produto pelo ID'''
    
    if not await validator.verify_product_id_exist(product_id, database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com id {product_id} não encontrado."
        )

    await services.delete_product(product_id, database)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@products_router.put('/{product_id}', response_model=schema.ShowProduct, status_code=status.HTTP_200_OK)
async def update_product_by_id(
    product_id: int, 
    request: schema.UpdateProduct,
    database: AsyncSession = Depends(db.get_db)
):
    '''Funcao para atualizar um produto pelo ID'''

    if not await validator.verify_product_id_exist(product_id, database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com id {product_id} não encontrado."
        )
    
    if not await validator.verify_category_id_exist(request.category_id, database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com id {request.category_id} não encontrada."
        )
    
    updated_product = await services.update_product(product_id, request, database)
    return updated_product


categories_router = APIRouter(tags=['Categories'], prefix='/categories')

@categories_router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.ShowCategory)
async def create_category(request: schema.Category, database: AsyncSession = Depends(db.get_db)):
    '''Funcao para criar uma nova categoria'''
    
    if await validator.verify_category_name_exist(request.name, database):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Categoria com o nome '{request.name}' já existe."
        )
    
    new_category = await services.create_new_category(request, database)
    return new_category

@categories_router.get('/', response_model=List[schema.ShowCategory], status_code=status.HTTP_200_OK)
async def get_all_categories(database: AsyncSession = Depends(db.get_db)):
    '''Funcao para obter todas as categorias'''
    return await services.list_all_categories(database)

@categories_router.get('/{category_id}', response_model=schema.ShowCategory, status_code=status.HTTP_200_OK)
async def get_category_by_id(category_id: int, database: AsyncSession = Depends(db.get_db)):
    '''Funcao para obter uma categoria pelo ID'''
    category = await services.get_category_by_id(category_id, database)
    
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Categoria com id {category_id} não encontrada."
        )
    return category

@categories_router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_category_by_id(category_id: int, database: AsyncSession = Depends(db.get_db)):
    '''Funcao para deletar uma categoria pelo ID'''
    
    if not await validator.verify_category_id_exist(category_id, database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com id {category_id} não encontrada."
        )

    await services.delete_category(category_id, database)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@categories_router.put('/{category_id}', response_model=schema.ShowCategory, status_code=status.HTTP_200_OK)
async def update_category_by_id(
    category_id: int, 
    request: schema.Category, 
    database: AsyncSession = Depends(db.get_db)
):
    '''Funcao para atualizar uma categoria pelo ID'''

    if not await validator.verify_category_id_exist(category_id, database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com id {category_id} não encontrada."
        )
    
    existing_category = await validator.verify_category_name_exist(request.name, database)
    if existing_category and existing_category.id != category_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Categoria com o nome '{request.name}' já existe."
        )

    return await services.update_category(category_id, request, database)