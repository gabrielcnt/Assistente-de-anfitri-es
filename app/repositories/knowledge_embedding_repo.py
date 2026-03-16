import json

from sqlalchemy.orm import Session

from app.models.knowledge_embedding import KnowledgeEmbedding


class KnowledgeEmbeddingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, entity, entity_id, content, vector):

        embedding_json = json.dumps(vector)

        registration = KnowledgeEmbedding(
            entity=entity,
            entity_id=entity_id,
            content=content,
            embedding=embedding_json,
        )

        self.db.add(registration)

        return registration

    def list_by_entity(self, entity, entity_id):
        return (
            self.db.query(KnowledgeEmbedding)
            .filter(
                KnowledgeEmbedding.entity == entity,
                KnowledgeEmbedding.entity_id == entity_id,
            )
            .all()
        )
