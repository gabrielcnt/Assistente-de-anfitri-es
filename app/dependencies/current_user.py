from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.repositories.user_repo import UserRepository
from app.core.jwt_token import SECRET_KEY, ALGORITHM
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    credencials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas"
    )

    try:
        print("TOKEN RECEBIDO:", token)
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        print("PAYLOAD:", payload)

        user_id = payload.get("sub")
        role = payload.get("role")

        print("USER_ID:", user_id)

        if user_id is None:
            raise credencials_exception
        
    except JWTError as e:
        print("ERRO JWT", str(e))
        raise credencials_exception
    
    user_repository = UserRepository(db)
    user = user_repository.get_by_id(int(user_id))

    user.token_role = role

    print("USER:", user)
    

    
    if not user:
        raise credencials_exception

    return user



def required_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permissão insuficiente"
        )
    
    return current_user



def block_if_password_change_required(current_user = Depends(get_current_user)):

    if current_user.token_role == "password_change_required":
        raise HTTPException(
            status_code=403,
            detail="Você precisa alterar sua senha antes de acessar o sistema."
        )
    return current_user