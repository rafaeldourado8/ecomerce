from sqlalchemy.orm import Session
from typing import Optional

from . models import User

def verify_email_exist(email: str, db_session: Session) -> Optional[User]:
    # Funcao para verificar se o usuario existe
    return db_session.query(User).filter(User.email == email).first()