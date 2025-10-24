from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db import get_db
from . import services
from . import schema

order_router = APIRouter(tags=['Orders'], prefix='/orders')

@order_router.post(
    '/', 
    status_code=status.HTTP_201_CREATED, 
    response_model=schema.ShowOrderDetails
)
async def create_order(
    user_email: str, 
    database: AsyncSession = Depends(get_db)
):
    '''Cria um novo pedido a partir do carrinho do usuário e limpa o carrinho.'''
    
    try:
        new_order = await services.create_order_from_cart(user_email, database)
        return new_order
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )

@order_router.get(
    '/', 
    response_model=List[schema.ShowOrder]
)
async def get_user_orders(
    user_email: str,
    database: AsyncSession = Depends(get_db)
):
    '''Lista todos os pedidos de um usuário (sem detalhes dos itens).'''
    
    orders = await services.list_orders_for_user(user_email, database)
    return orders

@order_router.get(
    '/{order_id}', 
    response_model=schema.ShowOrderDetails
)
async def get_order_details(
    order_id: int, 
    database: AsyncSession = Depends(get_db)
):
    '''Obtém os detalhes completos de um pedido específico.'''
    
    order = await services.get_order_by_id(order_id, database)
    return order