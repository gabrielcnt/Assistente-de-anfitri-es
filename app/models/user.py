from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, func
from sqlalchemy.orm import relationship
from app.core.config import db

class User(db.base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha_hash = Column(String, nullable=False)
    role = Column(Enum("admin", "user"), nullable=False)
    is_first_login = Column(Boolean, nullable=False, default=True)
    is_active = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    imoveis = relationship("Imovel", back_populates="user")