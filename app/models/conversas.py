from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime, timezone

from app.core.config import db

class Conversa(db.base):
    __tablename__ = "conversas"

    id = Column(Integer, autoincrement=True, primary_key=True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    hospede_id = Column(Integer, nullable=False)
    iniciado_em = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    encerrado_em = Column(DateTime(timezone=True), nullable=True)

    imovel = relationship("Imovel", back_populates="conversas")