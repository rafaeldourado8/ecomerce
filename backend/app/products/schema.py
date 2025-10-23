from pydantic import BaseModel, Field
from typing import Annotated, Optional

class Category(BaseModel):
    '''Schema para criar uma nova categoria'''
    name: Annotated[str, Field(min_length=2, max_length=50)]

class ShowCategory(BaseModel):
    '''Schema para exibir os dados da categoria'''
    id: int
    name: str

    class Config:
        from_attributes = True 

class Product(BaseModel):
    '''Schema para criar um novo produto'''
    name: Annotated[str, Field(min_length=3, max_length=100)]
    qtd: int
    description: Optional[str] = None 
    price: int
    category_id: int

class ShowProduct(BaseModel):
    '''Schema para exibir os dados do produto'''
    id: int
    name: str
    qtd: int
    description: Optional[str] = None
    price: int
    category: ShowCategory # Exibe a categoria aninhada

    class Config:
        from_attributes = True # 'orm_mode = True' do Pydantic v1

class UpdateProduct(BaseModel):
    '''Schema para atualizar um produto'''
    name: Annotated[str, Field(min_length=3, max_length=100)]
    qtd: int
    description: Optional[str] = None
    price: int
    category_id: int

class ProductId(BaseModel):
    '''Schema para representar o ID do produto'''
    id: int
    class Config:
        from_attributes = True