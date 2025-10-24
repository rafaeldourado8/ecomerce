from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional

from . models import User

async def verify_email_exist(email: str, db_session: AsyncSession) -> Optional[User]:
    '''Funcao para verificar se o usuario existe'''
    query = select(User).where(User.email == email)
    result = await db_session.execute(query)
    return result.scalars().first()