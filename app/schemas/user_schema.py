from pydantic import BaseModel, ConfigDict

from typing import Optional

from datetime import datetime

class UserSchemaCreate(BaseModel):
    username: str
    email: str
    senha: str
    role: str = "user"

class UserSchemaResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    is_first_login: bool
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserSchemaUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class UserSchemaUpdateAdmin(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    is_first_login: Optional[bool] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None

class UserSchemaAlterarSenha(BaseModel):
    senha_atual: str
    senha_nova: str
    confirmar_senha: str

class LoginRequest(BaseModel):
    email: str
    password: str