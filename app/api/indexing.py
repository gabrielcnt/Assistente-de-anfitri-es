from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.repositories.knowledge_embedding_repo import KnowledgeEmbeddingRepository
from app.repositories.property_repo import PropertyRepository
from app.services.embedding_service import EmbeddingService
from app.services.property_index_service import PropertyIndexService
from app.services.property_service import PropertyNotFoundError

router = APIRouter()


@router.post("/index/property/{property_id}")
def index_property(property_id: int, db: Session = Depends(get_db)):

    property_repository = PropertyRepository(db)
    property_obj = property_repository.get_by_id(property_id)

    if not property_obj:
        raise PropertyNotFoundError("Imóvel não encontrado")

    embedding_service = EmbeddingService()

    repository = KnowledgeEmbeddingRepository(db)

    index_service = PropertyIndexService(
        embedding_service=embedding_service, repository=repository, db=db
    )

    index_service.index_property(property_obj)

    return {"message": "Property indexed successfully"}
