from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship

from app.core.config import db

class Imovel(db.base):
    __tablename__ = "imoveis"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    
    regras = Column(Text, nullable=True)
    
    checkin_info = Column(Text, nullable=True)
    checkout_info = Column(Text, nullable=True)
    
    wifi_nome = Column(String, nullable=True)
    wifi_senha = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    user = relationship("User", back_populates="imoveis")
    conversas = relationship("Conversa", back_populates="imovel", cascade="all, delete-orphan")
    hospedes = relationship("Hospede", back_populates="imovel", cascade="all, delete-orphan")
    dicas_lugares = relationship("DicaLugar", back_populates="imovel", cascade="all, delete-orphan")