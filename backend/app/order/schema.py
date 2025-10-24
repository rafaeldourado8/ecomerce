from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

from app.products.schema import ShowProduct
from app.user.schema import ShowUser
from .models import OrderStatus

class ShowOrderItem(BaseModel):
    id: int
    quantity: int
    price_at_purchase: int
    product: ShowProduct | None 
    model_config = ConfigDict(from_attributes=True)

class OrderBase(BaseModel):
    pass

class ShowOrder(BaseModel):
    id: int
    total_price: int
    status: OrderStatus
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)

class ShowOrderDetails(ShowOrder):
    user: ShowUser
    items: List[ShowOrderItem] = []

    model_config = ConfigDict(from_attributes=True)