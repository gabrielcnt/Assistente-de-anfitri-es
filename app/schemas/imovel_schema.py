from pydantic import BaseModel, ConfigDict
from typing import Optional

class ImovelSchemaCreate(BaseModel):

    nome: str
    endereco: str
    regras: Optional[str] = None
    checkin_info: Optional[str] = None
    checkout_info: Optional[str] = None
    wifi_nome: Optional[str] = None
    wifi_senha: Optional[str] = None



class ImovelSchemaUpdate(BaseModel):
  
    nome: Optional[str] = None
    endereco: Optional[str] = None
    regras: Optional[str] = None
    checkin_info: Optional[str] = None
    checkout_info: Optional[str] = None
    wifi_nome: Optional[str] = None
    wifi_senha: Optional[str] = None



class ImovelSchemaResponse(BaseModel):

    id: int
    nome: str
    endereco: str
    regras: Optional[str] = None
    checkin_info: Optional[str] = None
    checkout_info: Optional[str] = None
    wifi_nome: Optional[str] = None
    wifi_senha: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)