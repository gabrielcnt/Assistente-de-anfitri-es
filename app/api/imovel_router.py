from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.config import get_db
from app.schemas.imovel_schema import ImovelSchemaCreate, ImovelSchemaUpdate, ImovelSchemaResponse
from app.services.imovel_service import ImovelService, ImovelNaoEncontrado, ImovelDuplicadoError
from app.repositories.imoveis_repo import ImovelRepository
from app.dependencies.current_user import get_current_user



router = APIRouter(prefix="/imoveis", tags=["Imoveis"])



@router.post("/", response_model=ImovelSchemaResponse, status_code=201)
def criar_imovel( imovel: ImovelSchemaCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        repo = ImovelRepository(db)
        service = ImovelService(db, repo)
        return service.criar_imovel(current_user.id, imovel)
    
    except ImovelDuplicadoError as e:
        raise HTTPException(status_code=409, detail=str(e))



@router.get("/", response_model=List[ImovelSchemaResponse], status_code=200)
def listar_imoveis_do_usuario(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    
    repo = ImovelRepository(db)
    service = ImovelService(db, repo)

    return service.listar_imoveis(current_user.id)



@router.patch("/{imovel_id}", response_model=ImovelSchemaResponse)
def atualizar_imovel(
    imovel_id: int,
    imovel_update: ImovelSchemaUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        repo = ImovelRepository(db)
        service = ImovelService(db, repo)
        
        return service.atualizar_imovel(current_user.id, imovel_id, imovel_update)
    
    except ImovelDuplicadoError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
    except ImovelNaoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))
    


@router.delete("/{imovel_id}")
def deletar_imovel(imovel_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        repo = ImovelRepository(db)
        service = ImovelService(db, repo)

        return service.apagar_imovel(current_user.id, imovel_id)
    
    except ImovelNaoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))