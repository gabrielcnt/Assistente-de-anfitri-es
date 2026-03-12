from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.schemas.user_schema import LoginRequest
from app.services.auth_service import AuthService, CredencialInvalida
from app.repositories.user_repo import UserRepository

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    try:
        user_repository = UserRepository(db)
        auth_service = AuthService(user_repository)
        
        return auth_service.login(
            email=data.email,
            password=data.password
        )
    except CredencialInvalida as e:
        raise HTTPException(status_code=401, detail=str(e))