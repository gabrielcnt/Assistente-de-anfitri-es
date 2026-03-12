from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.config import get_db
from app.schemas.dicas_lugares_schema import DicasLugaresSchemaResponse, DicasLugaresSchemaCreate, DicasLugaresSchemaUpdate
from app.services.dicas_lugares_service import DicaDuplicadaError, DicaNaoExisteError, PermissaoNegadaOuNaoExisteError, DicaLugarService
from app.repositories.dicas_lugares_repo import DicasLugaresRepository
from app.repositories.imoveis_repo import ImovelRepository
from app.dependencies.current_user import get_current_user

router = APIRouter(tags=["dicas de lugares"])


@router.post("/imoveis/{imovel_id}/dicas", response_model=DicasLugaresSchemaResponse, status_code=201)
def criar_dica(imovel_id: int, dica: DicasLugaresSchemaCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        repo_dica = DicasLugaresRepository(db)
        repo_imovel = ImovelRepository(db)
        service = DicaLugarService(db, repo_dica, repo_imovel)
        
        return service.criar_dica_lugar(current_user.id, imovel_id, dica)
    
    except DicaDuplicadaError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
    except DicaNaoExisteError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    except PermissaoNegadaOuNaoExisteError as e:
        raise HTTPException(status_code=404, detail=str(e))



@router.get("/imoveis/{imovel_id}/dicas", response_model=List[DicasLugaresSchemaResponse], status_code=201)
def listar_dicas_por_imovel(imovel_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    
    repo_dica = DicasLugaresRepository(db)
    repo_imovel = ImovelRepository(db)
    service = DicaLugarService(db, repo_dica, repo_imovel)
    

    return service.listar_dicas(current_user.id, imovel_id)



@router.patch("/imoveis/{imovel_id}/dicas/{dica_id}", response_model=DicasLugaresSchemaResponse)
def atualizar_dica(dica_id: int, imovel_id: int, dica_update: DicasLugaresSchemaUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        repo_dica = DicasLugaresRepository(db)
        repo_imovel = ImovelRepository(db)
        service = DicaLugarService(db, repo_dica, repo_imovel)

        return service.atualizar_dica(current_user.id, imovel_id, dica_id, dica_update)
    
    except DicaDuplicadaError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
    except DicaNaoExisteError as e:
        raise HTTPException(status_code=404, detail=str(e))
    


@router.delete("/imoveis/{imovel_id}/dicas/{dica_id}")
def deletar_dica(imovel_id: int, dica_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        repo_dica = DicasLugaresRepository(db)
        repo_imovel = ImovelRepository(db)
        service = DicaLugarService(db, repo_dica, repo_imovel)


        return service.apagar_dica(dica_id, imovel_id, current_user.id)
    except DicaNaoExisteError as e:
        raise HTTPException(status_code=404, detail=str(e))