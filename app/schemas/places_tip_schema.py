from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl


class PlacesTipsBase(BaseModel):
    description: Optional[str] = None
    cell_phone_number: Optional[str] = None
    map_link: Optional[HttpUrl] = None


class PlaceTip(str, Enum):
    restaurant = "restaurante"
    coffee = "cafe"
    bar = "bar"
    market = "mercado"
    pharmacy = "farmacia"
    hospital = "hospital"
    beach = "praia"
    tourist_attraction = "ponto_turistico"
    transport = "transporte"
    delivery = "delivery"
    emergency = "emergencia"


class PlacesTipSchemaCreate(PlacesTipsBase):
    type: PlaceTip
    name: str


class PlacesTipSchemaUpdate(PlacesTipsBase):
    type: Optional[PlaceTip] = None
    name: Optional[str] = None


class PlacesTipSchemaResponse(BaseModel):
    id: int
    property_id: int
    type: str
    name: str
    description: Optional[str] = None
    cell_phone_number: Optional[str] = None
    map_link: Optional[HttpUrl] = None

    model_config = ConfigDict(from_attributes=True)
