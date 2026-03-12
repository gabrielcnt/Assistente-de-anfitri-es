from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.schemas.user_schema import LoginRequest
from app.services.auth_service import AuthService
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
    
    user_repository = UserRepository(db)
    auth_service = AuthService(user_repository)
    
    return auth_service.login(
        email=data.email,
        password=data.password
    )