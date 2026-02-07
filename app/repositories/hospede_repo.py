from app.models.hospede import Hospede
from app.repositories.base_repo import BaseRepository


class HospedeRepository(BaseRepository):

    def get_by_id(self, hospede_id: int):
        return self.db.get(Hospede, hospede_id)
    
    def get_by_telefone_and_imovel(self, telefone: str, imovel_id: int):
        return self.db.query(Hospede).filter(
            Hospede.telefone == telefone,
            Hospede.imovel_id == imovel_id
            ).first()
    
    def list_by_imovel(self, imovel_id: int) -> list[Hospede]:
        return self.db.query(Hospede).filter(Hospede.imovel_id == imovel_id).all()
    