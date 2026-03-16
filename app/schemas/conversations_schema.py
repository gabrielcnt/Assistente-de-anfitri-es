from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class StatusConversation(str, Enum):
    active = "ATIVA"
    finished = "FINALIZADA"
    archived = "ARQUIVADA"


class ConversationCreate(BaseModel):
    user_id: int
    platform: str


class ConversationUpdate(BaseModel):
    status: Optional[StatusConversation] = None


class ConversationSchemaDashboardResponse(BaseModel):
    id: int
    started_in: datetime
    closed_in: Optional[datetime]
    status: StatusConversation
    property_name: str
    guest_name: str
    guest_phone: str

    model_config = ConfigDict(from_attributes=True)


class ConversationSchemaResponse(BaseModel):
    id: int
    property_id: int
    property_id: int
    started_in: datetime
    closed_in: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ConversationListResponse(BaseModel):
    total: int
    conversation: List[ConversationSchemaResponse]
