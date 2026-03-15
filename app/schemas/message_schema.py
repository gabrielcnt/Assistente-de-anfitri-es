from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MessageRole(str, Enum):
    guest = "hospede"
    agent = "agente"
    system = "sistema"


class TypeMessage(str, Enum):
    text = "texto"
    audio = "audio"
    image = "imagem"
    document = "documento"
    system = "sistema"


class MessageSchemaCreate(BaseModel):
    role: MessageRole
    content: Optional[str] = None
    type: TypeMessage = TypeMessage.text
    external_message_id: Optional[str] = None
    media_url: Optional[str] = None


class MessageSchemaResponse(BaseModel):
    id: int
    conversation_id: int
    role: MessageRole
    content: Optional[str] = None
    type: TypeMessage
    external_message_id: Optional[str]
    media_url: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
