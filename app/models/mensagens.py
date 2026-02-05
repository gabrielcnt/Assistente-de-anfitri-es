from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, func
from sqlalchemy.orm import relationship


from app.core.config import db

class Mensagem(db.base):
    __tablename__ = "mensagens"

    id = Column(Integer, primary_key=True)
    conversa_id = Column(Integer, ForeignKey("conversas.id"))
    #(hospede | agente | sistema)
    papel = Column(String, nullable=False)
    conteudo = Column(Text, nullable=False)
    criado_em = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    conversa = relationship("Conversa", back_populates="mensagens")
    