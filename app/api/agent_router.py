from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.property_agent import PropertyAgent
from app.core.config import get_db
from app.schemas.agent_schema import ChatRequest
from app.services.retrieval_service import RetrievalService
from app.services.embedding_service import EmbeddingService
from app.repositories.knowledge_embedding_repo import KnowledgeEmbeddingRepository

router = APIRouter(prefix="/assistente", tags=["Assistente"])


@router.post("/chat/imovel/{property_id}")
def chat_property(property_id: int, request: ChatRequest, db: Session = Depends(get_db)):

    embedding_service = EmbeddingService()
    repository = KnowledgeEmbeddingRepository(db)


    retrieval_service = RetrievalService(embedding_service, repository, db=db)

    agent = PropertyAgent(retrieval_service)

    question = request.question

    response = agent.to_ask(question)

    return {"response": response}
