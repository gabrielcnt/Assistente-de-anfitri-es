from app.repositories.dicas_lugares_repo import DicasLugaresRepository
from app.repositories.imoveis_repo import ImovelRepository
from app.schemas.dicas_lugares_schema import DicasLugaresSchemaCreate, DicasLugaresSchemaUpdate

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


class DicaDuplicadaError(Exception):
    pass

class ExisteImovelError(Exception):
    pass

class ExisteUsuarioError(Exception):
    pass

class DicaNaoExisteError(Exception):
    pass

class PermissaoNegadaOuNaoExisteError(Exception):
    pass

class DicasNaoEncontradasError(Exception):
    pass



class DicaLugarService:

    def __init__(self, db: Session, dicas_lugar_repo: DicasLugaresRepository, imovel_repo: ImovelRepository):
        self.dicas_lugar_repo = dicas_lugar_repo
        self.imovel_repo = imovel_repo
        self.db = db



    def criar_dica_lugar(self, user_id:int, imovel_id: int, dados: DicasLugaresSchemaCreate):
        imovel = self.imovel_repo.get_by_id_and_user(imovel_id, user_id)

        if not imovel:
            raise PermissaoNegadaOuNaoExisteError("Imóvel não existe ou não pertence ao usuário.")
           
        if self.dicas_lugar_repo.exists_by_nome(imovel_id, dados.nome):
            raise DicaDuplicadaError("Essa dica ja está cadastrada com esse nome.")
            
        try:

            nova_dica = self.dicas_lugar_repo.criar(imovel_id, dados)
            self.db.commit()
            self.db.refresh(nova_dica)

            return nova_dica
        
        except SQLAlchemyError:
            self.db.rollback()
            raise
    


    def listar_dicas(self, user_id: int, imovel_id: int):
            
        imovel = self.imovel_repo.get_by_id_and_user(imovel_id, user_id)
        
        if not imovel:
            raise PermissaoNegadaOuNaoExisteError("Imóvel não existe ou não pertence ao usuário")


        dica_lugar = self.dicas_lugar_repo.list_by_imovel(imovel_id)
        
        if not dica_lugar:
            raise DicasNaoEncontradasError("Nenhuma dica encontrada neste imovel")
        
        return dica_lugar
    


    
    def atualizar_dica(self, user_id: int, imovel_id: int, dica_id: int, dados: DicasLugaresSchemaUpdate):
        try:

            dica_lugar = self.dicas_lugar_repo.get_by_id_imovel_user(dica_id, imovel_id, user_id)

            if not dica_lugar:
                raise DicaNaoExisteError("Esta dica não existe ou não pertence ao usuário")

            if dados.nome is not None and dados.nome != dica_lugar.nome:
                if self.dicas_lugar_repo.exists_by_nome(imovel_id, dados.nome):
                    raise DicaDuplicadaError("Essa dica ja está cadastrada com esse nome.")
                
            for campo, valor in dados.model_dump(exclude_unset=True).items():
                setattr(dica_lugar, campo, valor)

            self.db.commit()
            self.db.refresh(dica_lugar)
            
            return dica_lugar
        
        except SQLAlchemyError:
            self.db.rollback()
            raise



    def apagar_dica(self, dica_id: int, imovel_id: int, user_id: int):
        try:
            
            dica_lugar = self.dicas_lugar_repo.get_by_id_imovel_user(dica_id, imovel_id, user_id)

            if not dica_lugar:
                raise DicaNaoExisteError("Esta dica não existe")
            
            self.dicas_lugar_repo.delete(dica_lugar)
            self.db.commit()

            return None
        
        except SQLAlchemyError:
            self.db.rollback()
            raise