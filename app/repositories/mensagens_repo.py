from app.repositories.base_repo import BaseRepository
from app.models.mensagens import Mensagem
from app.models.conversas import Conversa
from sqlalchemy import func

class MensagemRepository(BaseRepository):


    def get_by_id(self, mensagem_id: int):
        return self.db.get(Mensagem, mensagem_id)
    
    def get_by_mensagem_externa_id(self, mensagem_externa_id: str):
        return self.db.query(Mensagem).filter(Mensagem.mensagem_externa_id == mensagem_externa_id).first()

    def list_by_conversa(self, conversa_id: int):
        return self.db.query(Mensagem).filter(Mensagem.conversa_id == conversa_id).order_by(Mensagem.criado_em.asc()).all()
    
    def buscar_ultimas_mensagens(self, conversa_id: int, limit: int = 10):
        return self.db.query(Mensagem).filter(
            Mensagem.conversa_id == conversa_id
            ).order_by(Mensagem.criado_em.desc()).limit(limit).all()
        
    def count_by_mensagens(self, conversa_id: int):
        return self.db.query(func.count(Mensagem.id)).filter(Mensagem.conversa_id == conversa_id).scalar()
    
    def mensagens_papel(self, conversa_id: int, papel: str):
        return self.db.query(Mensagem).filter(Mensagem.conversa_id == conversa_id, Mensagem.papel == papel).all()
    
    