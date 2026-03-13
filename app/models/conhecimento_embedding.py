from sqlalchemy import Column, String, Integer, Text, DateTime
from datetime import datetime
from app.core.config import db

class ConhecimentoEmbedding(db.base):
    __tablename__ = "conhecimento_embedding"

    id = Column(Integer, primary_key=True)

    entidade = Column(String, nullable=False)
    entidade_id = Column(Integer, nullable=False)

    conteudo = Column(Text, nullable=False)
    embedding = Column(Text, nullable=False)
    
    created_at = Column(DateTime, default=datetime.now())