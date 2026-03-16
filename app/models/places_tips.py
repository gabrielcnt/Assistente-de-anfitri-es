from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from app.core.config import db


class PlaceTip(db.base):
    __tablename__ = "places_tips"

    id = Column(Integer, autoincrement=True, primary_key=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"))

    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    cell_phone_number = Column(String, nullable=True)
    map_link = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    property = relationship("Property", back_populates="places_tips")
