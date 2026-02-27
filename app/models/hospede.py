from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.config import db

from datetime import datetime, timezone

class Hospede(db.base):
    __tablename__ = "hospedes"

    id = Column(Integer, autoincrement=True, primary_key=True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    criado_em = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    conversa = relationship("Conversa", back_populates="hospede")
    imovel = relationship("Imovel", back_populates="imovel")