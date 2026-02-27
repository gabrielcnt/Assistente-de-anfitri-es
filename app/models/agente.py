from sqlalchemy import Column, String, Integer, Boolean, Text
from sqlalchemy.orm import relationship

from app.core.config import db

class Agente(db.base):
    __tablename__ = "agentes"

    id = Column(Integer, primary_key=True)

    nome = Column(String, nullable=True)
    personalidade_texto = Column(Text, nullable=True)
    tom_de_voz = Column(String, nullable=True)
    mensagem_boas_vindas = Column(Text, nullable=True)

    numero_whatsapp = Column(String, nullable=False)
    
    nivel_proatividade = Column(String, nullable=False)
    usar_emojis = Column(Boolean, nullable=False)
    idioma_padrao = Column(String, nullable=True, default="pt-br")
    
    avisos = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)

    imovel = relationship("Imovel", back_populates="agente")

    
    def disable(self):
        self.is_active = False