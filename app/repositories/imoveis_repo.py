from app.repositories.base_repo import BaseRepository
from app.models.imoveis import Imovel

class ImovelRepository(BaseRepository):

    def get_by_id(self, imovel_id: int):
        return self.db.get(Imovel, imovel_id)
    
    def list_by_user(self, user_id: int) -> list[Imovel]:
        return self.db.query(Imovel).filter(Imovel.user_id == user_id).all()
    
    def get_by_id_and_user(self, imovel_id: int, user_id: int):
        return self.db.query(Imovel).filter(Imovel.id == imovel_id, Imovel.user_id == user_id).first()
    
    def exists_by_nome(self, user_id: int, nome: str):
        return (self.db.query(Imovel).filter(Imovel.user_id == user_id, Imovel.nome == nome).first() is not None)
    
    def counter_by_user(self, user_id: int):
        return (self.db.query(Imovel).filter(Imovel.user_id == user_id).count())