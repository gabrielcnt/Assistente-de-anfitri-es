from app.repositories.base_repo import BaseRepository

from app.models.conversas import Conversa


class ConversaRepository(BaseRepository):


    def get_by_id(self, conversa_id: int):
        return self.db.get(Conversa, conversa_id).first()

    def get_conversa_ativa(self, imovel_id: int, hospede_id: int):
        return self.db.query(Conversa).filter(
            Conversa.imovel_id == imovel_id,
            Conversa.hospede_id == hospede_id,
            Conversa.status != "encerrada"
        ).all()
    
    def list_by_id_imovel(self, imovel_id: int):
        return self.db.query(Conversa).filter(Conversa.imovel_id == imovel_id).all()
    