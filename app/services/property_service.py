from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models.property import Property
from app.repositories.property_repo import PropertyRepository
from app.schemas.property_schema import PropertySchemaCreate, PropertySchemaUpdate


class DuplicatePropertyError(Exception):
    pass


class PropertyNotFoundError(Exception):
    pass


class PropertyService:
    def __init__(self, db: Session, property_repo: PropertyRepository):
        self.property_repo = property_repo
        self.db = db

    def create_property(self, user_id: int, dados: PropertySchemaCreate):
        try:
            if self.property_repo.exists_by_nome(user_id, dados.name):
                raise DuplicatePropertyError("Você já possui um imóvel com esse nome.")

            new_property = Property(user_id=user_id, **dados.model_dump())

            self.property_repo.add(new_property)
            self.db.commit()
            self.db.refresh(new_property)

            return new_property

        except SQLAlchemyError:
            self.db.rollback()
            raise

    def update_property(
        self, user_id: int, property_id: int, dados: PropertySchemaUpdate
    ):
        try:
            property = self.property_repo.get_by_id_and_user(property_id, user_id)

            if not property:
                raise PropertyNotFoundError("Imóvel não encontrado.")

            if dados.name is not None and dados.name != property.nome:
                if self.property_repo.exists_by_nome(user_id, dados.name):
                    raise DuplicatePropertyError(
                        "Você já possui um imóvel com esse nome."
                    )

            for campo, valor in dados.model_dump(exclude_unset=True).items():
                setattr(property, campo, valor)

            self.db.commit()
            self.db.refresh(property)

            return property

        except SQLAlchemyError:
            self.db.rollback()
            raise

    def delete_property(self, user_id: int, property_id: int):
        try:
            property = self.property_repo.get_by_id_and_user(property_id, user_id)

            if not property:
                raise PropertyNotFoundError("Imóvel não encontrado.")

            self.db.delete(property)
            self.db.commit()

            return None

        except SQLAlchemyError:
            self.db.rollback()
            raise

    def list_properties(self, user_id: int):

        return self.property_repo.list_by_user(user_id)
