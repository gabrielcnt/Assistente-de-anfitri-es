from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text, JSON

from app.core.config import db


class KnowledgeEmbedding(db.base):
    __tablename__ = "knowledge_embedding"

    id = Column(Integer, primary_key=True)

    entity = Column(String, nullable=False)
    entity_id = Column(Integer, nullable=False)

    content = Column(Text, nullable=False)
    embedding = Column(JSON, nullable=False)

    created_at = Column(DateTime, default=datetime.now())
