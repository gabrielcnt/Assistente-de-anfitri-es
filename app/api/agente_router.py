from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.config import get_db
from app.schemas.agente_schema import AgenteSchemaCreate, AgenteSchemaResponse, AgenteSchemaUpdate
from app.repositories.agente_repo import AgenteRepository

router = APIRouter(prefix="/assistente", tags=["Agente"])


@router.post("/", response_model=AgenteSchemaResponse, status_code=201)
def criar_assistente(agente: AgenteSchemaCreate, db: Session = Depends(get_db)):
    repo = AgenteRepository(db)
    user_id = 1
    return