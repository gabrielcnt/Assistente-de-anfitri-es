from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from enum import Enum

class PapelAgente(str, Enum):
    baixo = "baixo"
    medio = "medio"
    alto = "alto"

class AgenteBase(BaseModel):

    nome: Optional[str] = None
    personalidade_texto: Optional[str] = None
    tom_de_voz: Optional[str] = None
    mensagem_boas_vindas: Optional[str] = None
    avisos: Optional[str] = None



class AgenteSchemaCreate(AgenteBase):


    numero_whatsapp: str = Field(
        ...,
        min_length=11,
        max_length=14,
        pattern=r"^\d+$"
    )
    nivel_proatividade: PapelAgente
    usar_emojis: bool
    idioma_padrao: str
    is_active: Optional[bool] = None



class AgenteSchemaUpdate(AgenteBase):

    numero_whatsapp: Optional[str] = None
    nivel_proatividade: Optional[PapelAgente] = None
    usar_emojis: Optional[bool] = None
    idioma_padrao: Optional[str] = None
    is_active: Optional[bool] = None



class AgenteSchemaResponse(BaseModel):

    id: int
    nome: Optional[str] = None
    personalidade_texto: Optional[str] = None
    tom_de_voz: Optional[str] = None
    mensagem_boas_vindas: Optional[str] = None
    numero_whatsapp: str
    nivel_proatividade: PapelAgente
    usar_emojis: bool
    idioma_padrao: str
    avisos: Optional[str] = None
    is_active: bool
    model_config = ConfigDict(from_attributes=True)