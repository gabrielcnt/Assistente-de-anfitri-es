from app.models.dicas_lugares import DicaLugar
from app.repositories.base_repo import BaseRepository

class DicasLugaresRepository(BaseRepository):


    def get_by_id(self, dicas_lugares_id: int):
        return self.db.get(DicaLugar, dicas_lugares_id)

    # Listar dicas de lugares para um imovel
    def list_by_imovel(self, imovel_id: int) -> list[DicaLugar]:
        return self.db.query(DicaLugar).filter(DicaLugar.imovel_id == imovel_id).all()

    # Listar dicas de lugares para um imovel, filtrado por categoria
    def list_by_imovel_and_tipo(self, imovel_id:int, tipo: str) -> list[DicaLugar]:
        return self.db.query(DicaLugar).filter(DicaLugar.imovel_id == imovel_id, DicaLugar.tipo == tipo).all()

    # Verifica se uma dica com esse nome existe
    def exists_by_nome(self, imovel_id: int, nome: str) -> bool:
        return (
            self.db.query(DicaLugar.id).filter(
                DicaLugar.imovel_id == imovel_id,
                DicaLugar.nome == nome
                )
                .first()
                is not None
        )