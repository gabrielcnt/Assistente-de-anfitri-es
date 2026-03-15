from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.dependencies.current_user import block_if_password_change_required
from app.repositories.places_tip_repo import PlacesTipRepository
from app.repositories.property_repo import PropertyRepository
from app.schemas.places_tip_schema import (
    PlacesTipSchemaCreate,
    PlacesTipSchemaResponse,
    PlacesTipSchemaUpdate,
)
from app.services.places_tip_service import (
    DuplicateTipError,
    PermissionDeniedOrNotFoundError,
    PlaceTipService,
    TipNotFoundError,
)

router = APIRouter(tags=["dicas de lugares"])


@router.post(
    "/imoveis/{property_id}/dicas",
    response_model=PlacesTipSchemaResponse,
    status_code=201,
)
def create_tip(
    property_id: int,
    tip: PlacesTipSchemaCreate,
    db: Session = Depends(get_db),
    current_user=Depends(block_if_password_change_required),
):
    try:
        repo_tip = PlacesTipRepository(db)
        repo_property = PropertyRepository(db)
        service = PlaceTipService(db, repo_tip, repo_property)

        return service.create_place_ip(current_user.id, property_id, tip)

    except DuplicateTipError as e:
        raise HTTPException(status_code=409, detail=str(e))

    except TipNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except PermissionDeniedOrNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/imoveis/{property_id}/dicas",
    response_model=List[PlacesTipSchemaResponse],
    status_code=201,
)
def list_tip_by_property(
    property_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(block_if_password_change_required),
):

    repo_tip = PlacesTipRepository(db)
    repo_property = PropertyRepository(db)
    service = PlaceTipService(db, repo_tip, repo_property)

    return service.list_tips(current_user.id, property_id)


@router.patch(
    "/imoveis/{property_id}/dicas/{tip_id}", response_model=PlacesTipSchemaResponse
)
def update_tip(
    tip_id: int,
    property_id: int,
    tip_update: PlacesTipSchemaUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(block_if_password_change_required),
):

    try:
        repo_tip = PlacesTipRepository(db)
        repo_property = PropertyRepository(db)
        service = PlaceTipService(db, repo_tip, repo_property)

        return service.update_tip(current_user.id, property_id, tip_id, tip_update)

    except DuplicateTipError as e:
        raise HTTPException(status_code=409, detail=str(e))

    except TipNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/imoveis/{property_id}/dicas/{tip_id}")
def delete_tip(
    property_id: int,
    tip_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(block_if_password_change_required),
):
    try:
        repo_tip = PlacesTipRepository(db)
        repo_property = PropertyRepository(db)
        service = PlaceTipService(db, repo_tip, repo_property)

        return service.delete_tip(tip_id, property_id, current_user.id)
    except TipNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
