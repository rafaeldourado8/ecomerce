from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship
from app.db import Base
from . import hashing

class User(Base):
    '''Instancia a tabela Users a classe'''
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))


    def __repr__(self) -> str:
        return f"<User(id={self.id!r}, name={self.name!r}, email={self.email!r})>"
    
    def check_password(self, password):
        return hashing.verify_password(password, self.password)