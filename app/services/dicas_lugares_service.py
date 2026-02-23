from app.repositories.dicas_lugares_repo import DicasLugaresRepository
from app.repositories.imoveis_repo import ImovelRepository
from app.models.dicas_lugares import DicaLugar
from app.schemas.dicas_lugares_schema import DicasLugaresSchemaCreate, DicasLugaresSchemaUpdate

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


class DicaDuplicadaError(Exception):
    pass

class ExisteImovelError(Exception):
    pass

class ExisteUsuarioError(Exception):
    pass

class DicaExisteError(Exception):
    pass

class DicaLugarService:

    def __init__(self, db: Session, dicas_lugar_repo: DicasLugaresRepository, imovel_repo: ImovelRepository):
        self.dicas_lugar_repo = dicas_lugar_repo
        self.imovel_repo = imovel_repo
        self.db = db

    def criar_dica_lugar(self, user_id:int, imovel_id: int, dados: DicasLugaresSchemaCreate):
        try:
        
            if self.dicas_lugar_repo.exists_by_nome(imovel_id, dados.nome):
                raise DicaDuplicadaError("Essa dica ja está cadastrada com esse nome.")
            
            if not self.imovel_repo.get_by_id(imovel_id):
                raise ExisteImovelError("Não existe um imóvel para essa dica.")
            
            if not self.imovel_repo.get_by_id_and_user(imovel_id, user_id):
                raise ExisteUsuarioError("Não existe um usuário vinculado a este imovel")


            nova_dica = DicaLugar(
                imovel_id=imovel_id,
                **dados.model_dump()
            )
            self.dicas_lugar_repo.add(nova_dica)
            self.db.commit()
            self.db.refresh(nova_dica)
        
        except SQLAlchemyError:
            self.db.rollback()
            raise
    
    def atualizar_dica(self, user_id: int, imovel_id: int, dica_id: int, dados: DicasLugaresSchemaUpdate):
        try:

            dica_lugar = self.dicas_lugar_repo.get_by_id(dica_id)

            if not dica_lugar:
                raise DicaExisteError("Esta dica não existe")
            
            if dica_lugar.imovel_id != imovel_id or dica_lugar.user_id != user_id:
                raise ExisteUsuarioError("Esta dica não pertence a este imovel ou usuario")

            if dados.nome is not None and dados.nome != dica_lugar.nome:
                if self.dicas_lugar_repo.exists_by_nome(dados.nome):
                    raise DicaDuplicadaError("Essa dica ja está cadastrada com esse nome.")
                
            for campo, valor in dados.model_dump(exclude_unset=True).items():
                setattr(dica_lugar, campo, valor)

            self.db.commit()
            self.db.refresh(dica_lugar)

        except SQLAlchemyError:
            self.db.rollback()
            raise

    def apagar_dica(self, dica_id: int):
        try:
            
            dica_lugar = self.dicas_lugar_repo.get_by_id(dica_id)

            if not dica_lugar:
                raise DicaExisteError("Esta dica não existe")
            
            self.dicas_lugar_repo.delete(dica_lugar)
            self.db.commit()

            return None
        
        except SQLAlchemyError:
            self.db.rollback()
            raise