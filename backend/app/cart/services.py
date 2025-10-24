from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload, selectinload

from app.db import get_db
from app.user.models import User
from app.products.models import Product
from .models import Cart, CartItem 
from .schema import ShowCart
from . import schema

async def add_item_to_cart(product_id: int, user_email: str, database: AsyncSession):
    '''Funcao para adicionar um item ao carrinho de um usuario'''
    result = await database.execute(select(User).where(User.email == user_email))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    result = await database.execute(select(Cart).where(Cart.user_id == user.id))
    cart = result.scalars().first()
    
    if not cart:
        cart = Cart(user_id=user.id)
        database.add(cart)
        await database.commit()
        await database.refresh(cart)
    
    cart_item = CartItem(cart_id=cart.id, product_id=product_id) 
    database.add(cart_item)
    await database.commit()
    await database.refresh(cart_item) 

    query = (
        select(CartItem)
        .where(CartItem.id == cart_item.id)
        .options(
            joinedload(CartItem.product).joinedload(Product.category)
        )
    )
    
    result = await database.execute(query)
    final_cart_item = result.scalars().first()
    
    return final_cart_item

async def remove_item_from_cart(cart_item_id: int, database: AsyncSession) -> None:
    '''Funcao para remover um item do carrinho pelo seu ID'''
    
    query = select(CartItem).where(CartItem.id == cart_item_id)
    result = await database.execute(query)
    cart_item = result.scalars().first()
    
    if not cart_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item do carrinho com id {cart_item_id} não encontrado."
        )
    
    await database.delete(cart_item)
    await database.commit()

async def retrieve_cart_by_user_email(email: str, database: AsyncSession) -> Cart:
    '''Funcao para obter o carrinho de um usuario pelo email'''

    user_query = select(User).where(User.email == email)
    user_result = await database.execute(user_query)
    user = user_result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    cart_query = (
        select(Cart)
        .where(Cart.user_id == user.id)
        .options(
            selectinload(Cart.cart_item)
            .joinedload(CartItem.product)
            .joinedload(Product.category)
        )
    )
    
    result = await database.execute(cart_query)
    cart = result.scalars().first()
    return cart