from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserSchemaCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)
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


class UserSchemaChangePassword(BaseModel):
    current_password: str = Field(min_length=8, max_length=64)
    new_password: str = Field(min_length=8, max_length=64)
    confirm_password: str = Field(min_length=8, max_length=64)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)
