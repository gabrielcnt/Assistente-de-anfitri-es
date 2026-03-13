from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from datetime import datetime
from app.core.config import db

class ImovelEmbedding(db.base):
    __tablename__ = "imovel_embedding"

    id = Column(Integer, primary_key=True, index=True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    conteudo = Column(Text)
    embedding = Column(Text)
    
    created_at = Column(DateTime, default=datetime.now())