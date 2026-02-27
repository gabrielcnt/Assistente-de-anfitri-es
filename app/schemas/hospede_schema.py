from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class HospedeSchemaCreate(BaseModel):
    nome: str
    telefone: str = Field(
        ...,
        min_length=11,
        max_length=14,
        pattern=r"^\d+$"
    )



class HospedeSchemaUpdate(BaseModel):
    nome: Optional[str] = None
    telefone: Optional[str] = None



class HospedeSchemaResponse(BaseModel):
    id: int
    nome: str
    telefone: str

    model_config = ConfigDict(from_attributes=True)