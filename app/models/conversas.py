from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship

from datetime import datetime, timezone

from app.core.config import db

class Conversa(db.base):
    __tablename__ = "conversas"

    id = Column(Integer, autoincrement=True, primary_key=True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id", ondelete="CASCADE"), nullable=False)
    hospede_id = Column(Integer, ForeignKey("hospedes.id"), nullable=False)
    canal = Column(Enum("telegram", "whatsapp", name="canal_conversa"), nullable=False)
    status = Column(Enum(
        "ativa_ia", "ativa_humana",
        "encerrada", "aguardando_resposta_hospede",
        "transferida", "bloqueada", "erro"),
        nullable=False, default="ativa_ia")
    
    identificador_externo = Column(String, nullable=False)

    iniciado_em = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    encerrado_em = Column(DateTime(timezone=True), nullable=True)

    imovel = relationship("Imovel", back_populates="conversas")
    hospede = relationship("Hospede", back_populates="conversas")
    mensagens = relationship("Mensagem", back_populates="conversa", cascade="all, delete-orphan", order_by="Mensagem.criado_em")