from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.repositories.knowledge_embedding_repo import KnowledgeEmbeddingRepository
from app.services.embedding_service import EmbeddingService


class PropertyIndexService:
    def __init__(
        self,
        embedding_service: EmbeddingService,
        repository: KnowledgeEmbeddingRepository,
        db: Session,
    ):
        self.embedding_service = embedding_service
        self.repository = repository
        self.db = db

    def index_property(self, property):
        try:
            texts = [property.rules, property.checkin_info, property.checkout_info]

            for text in texts:
                if not text:
                    return

                vector = self.embedding_service.generate_embedding(text)

                registration = self.repository.create(
                    entity="property",
                    entity_id=property.id,
                    content=text,
                    vector=vector,
                )

            self.db.commit()
            self.db.refresh(registration)

            return registration

        except SQLAlchemyError:
            self.db.rollback()
            raise
