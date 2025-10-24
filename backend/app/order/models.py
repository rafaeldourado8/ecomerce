import enum
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, Numeric
from sqlalchemy.orm import relationship
from app.db import Base

class OrderStatus(str, enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    total_price = Column(Integer, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    created_date = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Order(id={self.id!r}, user_id={self.user_id!r}, status={self.status!r})>"

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.id", ondelete="SET NULL"), nullable=True) # Se o produto for deletado, o pedido o mantém (SET NULL)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Integer, nullable=False) # Snapshot do preço

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")

    def __repr__(self) -> str:
        return f"<OrderItem(id={self.id!r}, order_id={self.order_id!r}, product_id={self.product_id!r})>"