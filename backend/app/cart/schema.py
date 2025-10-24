import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict 

from app.products.schema import ShowProduct, Product
from app.user.schema import ShowUser


class CartItemBase(BaseModel):
    product_id: int
    quantity: int = 1

class CartItemCreate(CartItemBase):
    cart_id: int

class ShowCartItem(CartItemBase):
    id: int
    product: ShowProduct
    model_config = ConfigDict(from_attributes=True)

class CartBase(BaseModel):
    user_id: int

class CartCreate(CartBase):
    pass

class ShowCart(CartBase):
    id: int
    items: List[ShowCartItem] = []
    model_config = ConfigDict(from_attributes=True)

class ShowCartWithUser(ShowCart):
    user: ShowUser
    model_config = ConfigDict(from_attributes=True)

class CartUpdateQuantity(BaseModel):
    quantity: int