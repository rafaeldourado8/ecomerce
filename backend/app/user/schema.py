from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Annotated

class User(BaseModel):
    '''Schema para registrar um novo usuario'''
    name: Annotated[str, Field(min_length=2, max_length=50)]
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    '''Schema para exibir os dados do usuario'''
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)