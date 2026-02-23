from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List
from enum import Enum


class StatusConversa(str, Enum):
    ATIVA = "ATIVA"
    FINALIZADA = "FINALIZADA"
    ARQUIVADA = "ARQUIVADA"


class ConversaCreate(BaseModel):
    usuario_id: int
    plataforma: str



class ConversaUpdate(BaseModel):
    status: Optional[StatusConversa] = None



class ConversaSchemaDashboardResponse(BaseModel):
    
    id: int
    iniciado_em: datetime
    encerrado_em: Optional[datetime]
    status: StatusConversa
    imovel_nome: str
    hospede_nome: str
    hospede_telefone: str

    model_config = ConfigDict(from_attributes=True)



class ConversaSchemaResponse(BaseModel):
    
    id: int
    imovel_id: int
    hospede_id: int
    iniciado_em: datetime
    encerrado_em: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
    


class ConversaListResponse(BaseModel):
    total: int
    conversas: List[ConversaSchemaResponse]