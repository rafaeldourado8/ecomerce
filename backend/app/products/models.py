from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 
from app.db import Base


class Category(Base):
    '''Intancia a tabela Categorias a classe'''
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    
    products = relationship("Product", back_populates="category")

class Product(Base):
    '''Instancia a tabela Produtos a classe'''
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    qtd = Column(Integer, nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False) 
    category = relationship("Category", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")
    
    def __repr__(self) -> str: 
        '''Representacao em string do objeto Product'''
        return f"<Product(id={self.id!r}, name={self.name!r}, price={self.price!r})>"