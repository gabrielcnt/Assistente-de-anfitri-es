from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.dependencies.current_user import block_if_password_change_required
from app.repositories.property_repo import PropertyRepository
from app.schemas.property_schema import (
    PropertySchemaCreate,
    PropertySchemaResponse,
    PropertySchemaUpdate,
)
from app.services.property_service import (
    DuplicatePropertyError,
    PropertyNotFoundError,
    PropertyService,
)

router = APIRouter(prefix="/imoveis", tags=["Imoveis"])


@router.post("/", response_model=PropertySchemaResponse, status_code=201)
def create_property(
    property: PropertySchemaCreate,
    db: Session = Depends(get_db),
    current_user=Depends(block_if_password_change_required),
):
    try:
        repo = PropertyRepository(db)
        service = PropertyService(db, repo)
        return service.create_property(current_user.id, property)

    except DuplicatePropertyError as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/", response_model=List[PropertySchemaResponse], status_code=200)
def list_users_property(
    db: Session = Depends(get_db),
    current_user=Depends(block_if_password_change_required),
):

    repo = PropertyRepository(db)
    service = PropertyService(db, repo)

    return service.list_properties(current_user.id)


@router.patch("/{property_id}", response_model=PropertySchemaResponse)
def update_property(
    property_id: int,
    property_update: PropertySchemaUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(block_if_password_change_required),
):
    try:
        repo = PropertyRepository(db)
        service = PropertyService(db, repo)

        return service.update_property(current_user.id, property_id, property_update)

    except DuplicatePropertyError as e:
        raise HTTPException(status_code=409, detail=str(e))

    except PropertyNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{property_id}")
def delete_property(
    property_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(block_if_password_change_required),
):
    try:
        repo = PropertyRepository(db)
        service = PropertyService(db, repo)

        return service.delete_property(current_user.id, property_id)

    except PropertyNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
