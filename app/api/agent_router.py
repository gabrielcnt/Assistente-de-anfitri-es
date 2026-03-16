from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.repositories.agent_repo import AgentRepository
from app.schemas.agent_schema import AgentSchemaCreate, AgentSchemaResponse

router = APIRouter(prefix="/assistente", tags=["Agente"])


@router.post("/", response_model=AgentSchemaResponse, status_code=201)
def criate_assistant(agent: AgentSchemaCreate, db: Session = Depends(get_db)):
    repo = AgentRepository(db)
    user_id = 1
    return
