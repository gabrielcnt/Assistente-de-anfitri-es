from fastapi import APIRouter, Depends
from app.dependencies.current_user import required_admin

router = APIRouter()

@router.get("/admin-only")
def rota_teste_admin(current_user = Depends(required_admin)):
    return{"msg": f"Olá {current_user.email}, você é admin!"}