from app.repositories.base_repo import BaseRepository

from app.models.conversas import Conversa

class ConversaRepository(BaseRepository):


    def get_by_id(self, conversa_id: int):
        return self.db.get(Conversa, conversa_id)

    def get_open(self, imovel_id: int, hospede_id: int):
        return self.db.query(Conversa).filter(
            Conversa.imovel_id == imovel_id,
            Conversa.hospede_id == hospede_id,
            Conversa.encerrado_em == None
        ).first()