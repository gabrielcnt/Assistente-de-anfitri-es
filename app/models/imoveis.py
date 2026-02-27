from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.core.config import db

class Imovel(db.base):
    __tablename__ = "imoveis"

    id = Column(Integer, autoincrement=True, primary_key=True)
    agente_id = Column(Integer, ForeignKey("agentes.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    
    regras = Column(Text, nullable=True)
    
    checkin_info = Column(Text, nullable=True)
    checkout_info = Column(Text, nullable=True)
    
    wifi_nome = Column(String, nullable=True)
    wifi_senha = Column(String, nullable=True)

    user = relationship("User", back_populates="imoveis")
    agente = relationship("Agente", back_populates="imoveis")

    