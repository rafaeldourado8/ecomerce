from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.user.schema import ShowUser, User
from . import services
from . import schema


cart_router = APIRouter(tags=['Cart'], prefix='/cart')

@cart_router.post('/add/{product_id}', response_model=schema.ShowCartItem, status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int, user_email: str, database: AsyncSession = Depends(get_db)):
    '''Funcao para adicionar um produto ao carrinho de um usuario'''
    cart_item = await services.add_item_to_cart(product_id, user_email, database)
    return cart_item

@cart_router.delete('/{cart_item_id}', status_code=status.HTTP_204_NO_CONTENT)
async def remove_product_from_cart(cart_item_id: int, database: AsyncSession = Depends(get_db)):
    '''Funcao para remover um produto do carrinho de um usuario'''
    # Assumindo que services.remove_item_from_cart é uma função async
    await services.remove_item_from_cart(cart_item_id, database)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@cart_router.get('/{email}', response_model=schema.ShowCart, status_code=status.HTTP_200_OK)
async def get_cart_by_user_email(email: str, database: AsyncSession = Depends(get_db)):
    '''Funcao para obter o carrinho de um usuario pelo email'''
    # Assumindo que services.retrieve_cart_by_user_email é uma função async
    cart = await services.retrieve_cart_by_user_email(email, database)
    
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Carrinho para o email '{email}' não encontrado."
        )
    return cart