from typing import Optional

from pydantic import BaseModel, ConfigDict


class PropertySchemaCreate(BaseModel):
    name: str
    address: str
    rules: Optional[str] = None
    checkin_info: Optional[str] = None
    checkout_info: Optional[str] = None
    wifi_name: Optional[str] = None
    wifi_password: Optional[str] = None


class PropertySchemaUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    rule: Optional[str] = None
    checkin_info: Optional[str] = None
    checkout_info: Optional[str] = None
    wifi_name: Optional[str] = None
    wifi_password: Optional[str] = None


class PropertySchemaResponse(BaseModel):
    id: int
    name: str
    address: str
    rules: Optional[str] = None
    checkin_info: Optional[str] = None
    checkout_info: Optional[str] = None
    wifi_name: Optional[str] = None
    wifi_password: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
