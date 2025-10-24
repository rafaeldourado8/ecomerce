from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload, selectinload

from app.user.models import User
from app.cart.models import Cart, CartItem
from app.products.models import Product
from .models import Order, OrderItem, OrderStatus
from . import schema

async def create_order_from_cart(user_email: str, database: AsyncSession) -> Order:
    '''Cria um pedido a partir do carrinho de um usuário e esvazia o carrinho.'''
    user_query = select(User).where(User.email == user_email)
    user_result = await database.execute(user_query)
    user = user_result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    cart_query = (
        select(Cart)
        .where(Cart.user_id == user.id)
        .options(
            joinedload(Cart.cart_item).joinedload(CartItem.product)
        )
    )
    cart_result = await database.execute(cart_query)
    cart = cart_result.scalars().first()

    if not cart or not cart.cart_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cart is empty.")
    total_price = 0
    order_items_to_create = []
    
    for item in cart.cart_item:
        if item.product:
            total_price += item.quantity * item.product.price
            order_items_to_create.append(
                OrderItem(
                    product_id=item.product.id,
                    quantity=item.quantity,
                    price_at_purchase=item.product.price
                )
            )
    new_order = Order(
        user_id=user.id,
        total_price=total_price,
        status=OrderStatus.PENDING,
        items=order_items_to_create 
    )
    
    database.add(new_order)
    await database.commit()
    await database.refresh(new_order)
    
    final_order = await get_order_by_id(new_order.id, database)
    return final_order


async def list_orders_for_user(user_email: str, database: AsyncSession) -> list[Order]:
    '''Lista todos os pedidos (sem detalhes dos itens) para um usuário.'''
    
    query = (
        select(Order)
        .join(User)
        .where(User.email == user_email)
        .order_by(Order.created_date.desc())
    )
    result = await database.execute(query)
    return result.scalars().all()


async def get_order_by_id(order_id: int, database: AsyncSession) -> Order:
    '''Obtém um pedido específico com todos os detalhes (usuário, itens, produtos).'''
    
    query = (
        select(Order)
        .where(Order.id == order_id)
        .options(
            joinedload(Order.user),
            selectinload(Order.items).joinedload(OrderItem.product).joinedload(Product.category)
        )
    )
    
    result = await database.execute(query)
    order = result.scalars().first()
    
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {order_id} not found.")
        
    return order