from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.repositories.places_tip_repo import PlacesTipRepository
from app.repositories.property_repo import PropertyRepository
from app.schemas.places_tip_schema import (
    PlacesTipSchemaCreate,
    PlacesTipSchemaUpdate,
)


class DuplicateTipError(Exception):
    pass


class ExistsPropertyError(Exception):
    pass


class ExistsUserError(Exception):
    pass


class TipNotFoundError(Exception):
    pass


class PermissionDeniedOrNotFoundError(Exception):
    pass


class TipsNotFoundError(Exception):
    pass


class PlaceTipService:
    def __init__(
        self,
        db: Session,
        place_tip_repo: PlacesTipRepository,
        property_repo: PropertyRepository,
    ):
        self.place_tip_repo = place_tip_repo
        self.property_repo = property_repo
        self.db = db

    def create_place_ip(
        self, user_id: int, property_id: int, dados: PlacesTipSchemaCreate
    ):
        imovel = self.property_repo.get_by_id_and_user(property_id, user_id)

        if not imovel:
            raise PermissionDeniedOrNotFoundError(
                "Imóvel não existe ou não pertence ao usuário."
            )

        if self.place_tip_repo.exists_by_name(property_id, dados.name):
            raise DuplicateTipError("Essa dica ja está cadastrada com esse nome.")

        try:
            new_tip = self.place_tip_repo.create(property_id, dados)
            self.db.commit()
            self.db.refresh(new_tip)

            return new_tip

        except SQLAlchemyError:
            self.db.rollback()
            raise

    def list_tips(self, user_id: int, property_id: int):

        property = self.property_repo.get_by_id_and_user(property_id, user_id)

        if not property:
            raise PermissionDeniedOrNotFoundError(
                "Imóvel não existe ou não pertence ao usuário"
            )

        place_tip = self.place_tip_repo.list_by_property(property_id)

        if not place_tip:
            raise TipsNotFoundError("Nenhuma dica encontrada neste imovel")

        return place_tip

    def update_tip(
        self,
        user_id: int,
        property_id: int,
        tip_id: int,
        dados: PlacesTipSchemaUpdate,
    ):
        try:
            place_tip = self.place_tip_repo.get_by_id_property_user(
                tip_id, property_id, user_id
            )

            if not place_tip:
                raise TipNotFoundError(
                    "Esta dica não existe ou não pertence ao usuário"
                )

            if dados.name is not None and dados.name != place_tip.nome:
                if self.place_tip_repo.exists_by_name(property_id, dados.name):
                    raise DuplicateTipError(
                        "Essa dica ja está cadastrada com esse nome."
                    )

            for campo, valor in dados.model_dump(exclude_unset=True).items():
                setattr(place_tip, campo, valor)

            self.db.commit()
            self.db.refresh(place_tip)

            return place_tip

        except SQLAlchemyError:
            self.db.rollback()
            raise

    def delete_tip(self, tip_id: int, property_id: int, user_id: int):
        try:
            place_tip = self.place_tip_repo.get_by_id_property_user(
                tip_id, property_id, user_id
            )

            if not place_tip:
                raise TipNotFoundError("Esta dica não existe")

            self.place_tip_repo.delete(place_tip)
            self.db.commit()

            return None

        except SQLAlchemyError:
            self.db.rollback()
            raise
