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


async def retrieve_all_users(database) -> list[models.User]:
    users = database.query(models.User).all()
    return users

async def retrieve_user_by_id(user_id: int, database) -> models.User:
    user = database.query(models.User).filter(models.User.id == user_id).first() 
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.") 
    return user 

async def delete_user(user_id: int, database) -> None:
    user = await retrieve_user_by_id(user_id, database)
    database.delete(user)
    database.commit()


