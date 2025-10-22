from fastapi import HTTPException, status
from . import models
from . import hashing  

async def new_user_register(request, database) -> models.User:
    hashed_password = hashing.get_password_hash(request.password)
    
    new_user = models.User(
        name=request.name, 
        email=request.email, 
        password=hashed_password  
    )
    
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user