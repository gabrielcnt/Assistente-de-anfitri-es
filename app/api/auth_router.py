from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.schemas.user_schema import LoginRequest, UserSchemaAlterarSenha
from app.services.auth_service import AuthService, CredencialInvalida, SenhaAtualIncorreta, SenhasDiferentesError
from app.repositories.user_repo import UserRepository
from app.dependencies.current_user import get_current_user



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
        auth_service = AuthService(user_repository, db)
        
        return auth_service.login(
            email=data.email,
            senha=data.senha
        )
    except CredencialInvalida as e:
        raise HTTPException(status_code=401, detail=str(e))


 
@router.post("/change-password")
def change_password(data: UserSchemaAlterarSenha, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    
    try:
        User_repository = UserRepository(db)
        auth_service = AuthService(User_repository, db)

        token = auth_service.change_password(
            current_user,
            data.senha_atual,
            data.senha_nova,
            data.confirmar_senha
        )


        return {
            "msg": "Senha alterada com sucesso",
            "access_token": token,
            "token_type": "bearer" 
        }
    
    except SenhaAtualIncorreta as e:
        raise HTTPException(status_code=401, detail=str(e))
    
    except SenhasDiferentesError as e:
        raise HTTPException(status_code=422, detail=str(e))

