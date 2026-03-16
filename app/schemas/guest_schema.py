from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class GuestSchemaCreate(BaseModel):
    name: str
    cell_phone_number: str = Field(..., min_length=11, max_length=14, pattern=r"^\d+$")


class GuestSchemaUpdate(BaseModel):
    name: Optional[str] = None
    cell_phone_number: Optional[str] = None


class GuestSchemaResponse(BaseModel):
    id: int
    name: str
    cell_phone_number: str

    model_config = ConfigDict(from_attributes=True)
