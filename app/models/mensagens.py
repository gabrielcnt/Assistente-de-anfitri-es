from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, func, Enum
from sqlalchemy.orm import relationship


from app.core.config import db

class Mensagem(db.base):
    __tablename__ = "mensagens"

    id = Column(Integer, primary_key=True)
    conversa_id = Column(Integer, ForeignKey("conversas.id", ondelete="CASCADE"), nullable=False)
    #(hospede | agente | sistema)
    papel = Column(Enum("HOSPEDE", "IA", "HUMANO", name="papel_mensagem"), nullable=False)
    tipo = Column(Enum("texto", "audio", "imagem", "documento", name="tipo_mensagem"))
    media_url = Column(String, nullable=True)
    mensagem_externa_id = Column(String, nullable=True, index=True)
    conteudo = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    conversa = relationship("Conversa", back_populates="mensagens")
    
    