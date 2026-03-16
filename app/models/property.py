from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from app.core.config import db


class Property(db.base):
    __tablename__ = "properties"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    rules = Column(Text, nullable=True)

    checkin_info = Column(Text, nullable=True)
    checkout_info = Column(Text, nullable=True)

    wifi_name = Column(String, nullable=True)
    wifi_password = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    user = relationship("User", back_populates="properties")
    conversations = relationship(
        "Conversation", back_populates="property", cascade="all, delete-orphan"
    )
    guest = relationship(
        "Guest", back_populates="property", cascade="all, delete-orphan"
    )
    places_tips = relationship(
        "PlaceTip", back_populates="property", cascade="all, delete-orphan"
    )
