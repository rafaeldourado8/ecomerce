from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models
from . import hashing  

async def new_user_register(request: models.User, database: AsyncSession) -> models.User:
    hashed_password = hashing.get_password_hash(request.password)
    
    new_user = models.User(
        name=request.name, 
        email=request.email, 
        password=hashed_password  
    )
    
    database.add(new_user)
    await database.commit()
    await database.refresh(new_user)
    return new_user


async def retrieve_all_users(database: AsyncSession) -> list[models.User]:
    query = select(models.User)
    result = await database.execute(query)
    users = result.scalars().all()
    return users

async def retrieve_user_by_id(user_id: int, database: AsyncSession) -> models.User:
    query = select(models.User).where(models.User.id == user_id)
    result = await database.execute(query)
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.") 
    return user 

async def get_user_filter_by_email(email: str, database: AsyncSession) -> models.User:
    query = select(models.User).where(models.User.email == email)
    result = await database.execute(query)
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user

async def delete_user(user_id: int, database: AsyncSession) -> None:
    user = await retrieve_user_by_id(user_id, database)
    await database.delete(user)
    await database.commit()