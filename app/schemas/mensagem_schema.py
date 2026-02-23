from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum
from datetime import datetime


class PapelMensagem(str, Enum):
    hospede = "hospede"
    agente = "agente"
    sistema = "sistema"


class TipoMensagem(str, Enum):
    texto = "texto"
    audio = "audio"
    imagem = "imagem"
    documento = "documento"
    sistema = "sistema"


class MensagemSchemaCreate(BaseModel):
    papel: PapelMensagem
    conteudo: Optional[str] = None
    tipo: TipoMensagem = TipoMensagem.texto
    mensagem_externa_id: Optional[str] = None
    arquivo_url: Optional[str] = None


class MensagemSchemaResponse(BaseModel):
    id: int
    conversa_id: int
    papel: PapelMensagem
    conteudo: Optional[str] = None
    tipo: TipoMensagem
    mensagem_externa_url: Optional[str]
    arquivo_url: Optional[str]
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)