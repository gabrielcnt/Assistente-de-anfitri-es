from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.config import db


class Guest(db.base):
    __tablename__ = "guests"

    id = Column(Integer, autoincrement=True, primary_key=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    cell_phone_number = Column(String, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    conversations = relationship("Conversation", back_populates="guest")
    property = relationship("Property", back_populates="guest")
