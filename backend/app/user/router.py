from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import db
from . import services
from . import schema
from . import validator

router = APIRouter(tags=['Users'], prefix='/user')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: AsyncSession = Depends(db.get_db)):
    '''Funcao para registrar um novo usuario'''

    user = await validator.verify_email_exist(request.email, database)
    
    if user:
        raise HTTPException(status_code=400, detail="The user with this email already exists in the system.",)
    
    new_user = await services.new_user_register(request, database)
    return new_user


@router.get('/', response_model=List[schema.ShowUser], status_code=status.HTTP_200_OK)
async def get_all_users(database: AsyncSession = Depends(db.get_db)):
    '''Funcao para obter todos os usuarios'''
    users = await services.retrieve_all_users(database)
    return users

@router.get('/{user_id}', response_model=schema.ShowUser, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, database: AsyncSession = Depends(db.get_db)):
    '''Funcao para obter um usuario pelo ID'''
    user = await services.retrieve_user_by_id(user_id, database)
    return user

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_id(user_id: int, database: AsyncSession = Depends(db.get_db)):
    '''Funcao para deletar um usuario pelo ID'''
    await services.delete_user(user_id, database)
    return Response(status_code=status.HTTP_204_NO_CONTENT)