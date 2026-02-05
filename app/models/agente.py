from sqlalchemy import Column, String, Integer, Boolean, Text

from app.core.config import db

class Agente(db.base):
    __tablename__ = "agentes"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)
    personalidade_texto = Column(Text, nullable=True)
    tom_de_voz = Column(String, nullable=True)
    usar_emojis = Column(Boolean, nullable=True)
    nivel_proatividade = Column(String, nullable=True)
    mensagem_boas_vindas = Column(Text, nullable=True)
    idioma_padrão = Column(String, nullable=True, default="pt-br")
    