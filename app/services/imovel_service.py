from app.repositories.imoveis_repo import ImovelRepository
from app.models.imoveis import Imovel
from app.schemas.imovel_schema import ImovelSchemaCreate, ImovelSchemaUpdate
from sqlalchemy.orm import Session

from sqlalchemy.exc import SQLAlchemyError


class ImovelDuplicadoError(Exception):
    pass

class ImovelNaoEncontrado(Exception):
    pass



class ImovelService:
    def __init__(self, db: Session, imovel_repo: ImovelRepository):
        self.imovel_repo = imovel_repo
        self.db = db

    
    def criar_imovel(self, user_id: int, dados: ImovelSchemaCreate):
        try:
            if self.imovel_repo.exists_by_nome(user_id, dados.nome):
                raise ImovelDuplicadoError("Você já possui um imóvel com esse nome.")
            
            novo_imovel = Imovel(
                user_id=user_id,
                **dados.model_dump())

            self.imovel_repo.add(novo_imovel)
            self.db.commit()
            self.db.refresh(novo_imovel)

            return novo_imovel
        
        except SQLAlchemyError:
            self.db.rollback()
            raise


    def atualizar_imovel(self, user_id: int, imovel_id: int , dados: ImovelSchemaUpdate):
        try:
            
            imovel = self.imovel_repo.get_by_id_and_user(imovel_id, user_id)

            if not imovel:
                raise ImovelNaoEncontrado("Imóvel não encontrado.")
            
            if dados.nome is not None and dados.nome != imovel.nome:
                if self.imovel_repo.exists_by_nome(user_id, dados.nome):
                    raise ImovelDuplicadoError("Você já possui um imóvel com esse nome.")
                
            for campo, valor in dados.model_dump(exclude_unset=True).items():
                setattr(imovel, campo, valor)

            self.db.commit()
            self.db.refresh(imovel)

            return imovel
        
        except SQLAlchemyError:
            self.db.rollback()
            raise
    

    def apagar_imovel(self, user_id: int, imovel_id: int):
        try:
            imovel = self.imovel_repo.get_by_id_and_user(imovel_id, user_id)

            if not imovel:
                raise ImovelNaoEncontrado("Imóvel não encontrado.")
            

            self.db.delete(imovel)
            self.db.commit()

            return None
        
        except SQLAlchemyError:
            self.db.rollback()
            raise

    
    def listar_imoveis(self, user_id: int):
        
        return self.imovel_repo.list_by_user(user_id)
