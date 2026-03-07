from app.models.dicas_lugares import DicaLugar
from app.repositories.base_repo import BaseRepository
from app.models.imoveis import Imovel



class DicasLugaresRepository(BaseRepository):

    def criar(self, imovel_id: int, dados) -> DicaLugar:
        data = dados.model_dump()

        if data.get("map_link"):
            data["map_link"] = str(data["map_link"])
        if data.get("tipo"):
            data["tipo"] = str(data["tipo"])
        dica = DicaLugar(
            imovel_id=imovel_id,
            **data
        )

        self.db.add(dica)
        return dica
    

    
    def get_by_id(self, dicas_lugares_id: int):
        return self.db.get(DicaLugar, dicas_lugares_id)

    def get_by_id_imovel_user(self, dica_id: int, imovel_id: int, user_id: int):
        return (
            self.db.query(DicaLugar)
            .join(Imovel)
            .filter(
                DicaLugar.id == dica_id,
                DicaLugar.imovel_id == imovel_id,
                Imovel.user_id == user_id
            )
            .first()
        )

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