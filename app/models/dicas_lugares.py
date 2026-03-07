from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.core.config import db

class DicaLugar(db.base):
    __tablename__ = "dicas_lugares"

    id = Column(Integer, autoincrement=True, primary_key=True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id", ondelete="CASCADE"))

    tipo = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    
    telefone = Column(String, nullable=True)
    map_link = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    imovel = relationship("Imovel", back_populates="dicas_lugares")
