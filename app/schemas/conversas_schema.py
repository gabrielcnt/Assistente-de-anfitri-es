from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ConversaSchemaDashboardResponse(BaseModel):
    
    id: int
    iniciado_em: datetime
    encerrado_em: Optional[datetime]
    imovel_nome: str
    hospede_nome: str
    hospede_telefone: str



class ConversaSchemaResponse(BaseModel):
    
    id: int
    imovel_id: int
    hospede_id: int
    iniciado_em: datetime
    encerrado_em: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)