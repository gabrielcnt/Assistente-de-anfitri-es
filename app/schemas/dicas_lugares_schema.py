from pydantic import BaseModel, ConfigDict, HttpUrl
from typing import Optional
from enum import Enum


class DicasLugaresBase(BaseModel):
    descricao: Optional[str] = None
    telefone: Optional[str] = None
    map_link: Optional[HttpUrl] = None


class TipoDica(str, Enum):
    restaurante = "restaurante"
    cafe = "cafe"
    bar = "bar"
    mercado = "mercado"
    farmacia = "farmacia"
    hospital = "hospital"
    praia = "praia"
    ponto_turistico = "ponto_turistico"
    transporte = "transporte"
    delivery = "delivery"
    emergencia = "emergencia"



class DicasLugaresSchemaCreate(DicasLugaresBase):
    tipo: TipoDica
    nome: str



class DicasLugaresSchemaUpdate(DicasLugaresBase):
    tipo: Optional[TipoDica] = None
    nome: Optional[str] = None



class DicasLugaresSchemaResponse(BaseModel):
    id:int
    imovel:int
    tipo: TipoDica
    nome: str
    descricao: Optional[str] = None
    telefone: Optional[str] = None
    map_link: Optional[HttpUrl] = None

    model_config = ConfigDict(from_attributes=True)
