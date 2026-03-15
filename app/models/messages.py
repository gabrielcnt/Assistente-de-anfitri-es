from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from app.core.config import db


class Message(db.base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    conversation_id = Column(
        Integer, ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False
    )
    # (hospede | agente | sistema)
    role = Column(Enum("guest", "IA", "human", name="role_message"), nullable=False)
    type = Column(Enum("text", "audio", "image", "document", name="type_message"))
    media_url = Column(String, nullable=True)
    external_message_id = Column(String, nullable=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    conversation = relationship("Conversation", back_populates="message")
