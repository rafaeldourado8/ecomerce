from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload 

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