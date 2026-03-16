from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class RoleAgent(str, Enum):
    low = "baixo"
    medium = "medio"
    high = "alto"


class AgentBase(BaseModel):
    name: Optional[str] = None
    personality_text: Optional[str] = None
    tone_of_voice: Optional[str] = None
    welcome_message: Optional[str] = None
    warning: Optional[str] = None


class AgentSchemaCreate(AgentBase):
    number_whatsapp: str = Field(..., min_length=11, max_length=14, pattern=r"^\d+$")
    proactivity_level: RoleAgent
    use_emojis: bool
    default_language: str
    is_active: Optional[bool] = None


class AgentSchemaUpdate(AgentBase):
    number_whatsapp: Optional[str] = None
    proactivity_level: Optional[RoleAgent] = None
    use_emojis: Optional[bool] = None
    default_language: Optional[str] = None
    is_active: Optional[bool] = None


class AgentSchemaResponse(BaseModel):
    id: int
    nome: Optional[str] = None
    personality_text: Optional[str] = None
    tone_of_voice: Optional[str] = None
    welcome_message: Optional[str] = None
    number_whatsapp: str
    proactivity_level: RoleAgent
    use_emojis: bool
    default_language: str
    warning: Optional[str] = None
    is_active: bool
    model_config = ConfigDict(from_attributes=True)


class ChatRequest(BaseModel):
    question: str