from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.config import db


class Conversation(db.base):
    __tablename__ = "conversations"

    id = Column(Integer, autoincrement=True, primary_key=True)
    imovel_id = Column(
        Integer, ForeignKey("property.id", ondelete="CASCADE"), nullable=False
    )
    hospede_id = Column(Integer, ForeignKey("guests.id"), nullable=False)
    canal = Column(Enum("telegram", "whatsapp", name="talk_channel"), nullable=False)
    status = Column(
        Enum(
            "ativa_ia",
            "ativa_humana",
            "encerrada",
            "aguardando_resposta_hospede",
            "transferida",
            "bloqueada",
            "erro",
        ),
        nullable=False,
        default="ativa_ia",
    )

    external_identifier = Column(String, nullable=False)

    started_in = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    closed_in = Column(DateTime(timezone=True), nullable=True)

    property = relationship("Property", back_populates="conversations")
    guest = relationship("Guest", back_populates="conversations")
    message = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan",
        order_by="Message.created_at",
    )
