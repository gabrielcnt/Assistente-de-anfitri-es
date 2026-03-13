from pydantic import BaseModel, ConfigDict, EmailStr, Field

from typing import Optional

from datetime import datetime

class UserSchemaCreate(BaseModel):
    username: str
    email: EmailStr
    senha: str = Field(min_length=8, max_length=64)
    role: str = "user"

class UserSchemaResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    is_first_login: bool
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserSchemaUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class UserSchemaUpdateAdmin(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_first_login: Optional[bool] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None

class UserSchemaAlterarSenha(BaseModel):
    senha_atual: str = Field(min_length=8, max_length=64)
    senha_nova: str = Field(min_length=8, max_length=64)
    confirmar_senha: str = Field(min_length=8, max_length=64)

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str = Field(min_length=8, max_length=64)