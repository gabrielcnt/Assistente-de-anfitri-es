from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum

class PapelMensagem(str, Enum):
    hospede = "hospede"
    agente = "agente"
    sistema = "sistema"

class MensagemSchemaCreate(BaseModel):
    papel: PapelMensagem
    conteudo: str


class MensagemSchemaUpdate(BaseModel):
    papel: Optional[PapelMensagem]
    conteudo: Optional[str] = None


class MensagemSchemaResponse(BaseModel):
    id: int
    conversa_id: int
    papel: PapelMensagem
    conteudo: str

    model_config = ConfigDict(from_attributes=True)