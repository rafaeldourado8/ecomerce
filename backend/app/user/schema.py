from pydantic import BaseModel, Field, EmailStr
from typing import Annotated

class User(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50)]
    email: EmailStr
    password: str

