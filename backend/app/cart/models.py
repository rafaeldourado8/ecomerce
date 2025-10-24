from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship as Relationship

from app.db import Base
from app.user.models import User
from app.products.models import Product


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE")) 
    cart_item = Relationship("CartItem", back_populates="cart") 
    user_cart = Relationship("User", back_populates="cart")
    created_date = Column(DateTime, default=datetime.now) #

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey("carts.id", ondelete = "CASCADE"))
    product_id = Column(Integer, ForeignKey("products.id", ondelete = "CASCADE"))
    cart = Relationship("Cart", back_populates="cart_item")
    products = Relationship("Product", back_populates="cart_items")
    created_date = Column(DateTime, default=datetime.now) 
    
    def __repr__(self) -> str:
        '''Representacao em string do objeto CartItem'''
        return f"<CartItem(id={self.id!r}, cart_id={self.cart_id!r}, product_id={self.product_id!r})>"
    

    