from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.repositories.knowledge_embedding_repo import KnowledgeEmbeddingRepository
from app.services.embedding_service import EmbeddingService


class TipsIndexService:
    def __init__(
        self,
        embedding_service: EmbeddingService,
        repository: KnowledgeEmbeddingRepository,
        db: Session,
    ):
        self.embedding_service = embedding_service
        self.repository = repository
        self.db = db

    def index_tips(self, tip):

        try:
            description = tip.description or ""

            text = f"""
            Lugar: {tip.name}
            Tipo: {tip.type}
            Descrição: {description}
            """

            vector = self.embedding_service.generate_embedding(text)

            registration = self.repository.create(
                entity="place_tip", entity_id=tip.id, content=text, vector=vector
            )

            self.db.commit()
            self.db.refresh(registration)

            return registration

        except SQLAlchemyError:
            self.db.rollback()
            raise
