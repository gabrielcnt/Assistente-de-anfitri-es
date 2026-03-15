from app.models.property import Property
from app.repositories.base_repo import BaseRepository


class PropertyRepository(BaseRepository):
    def get_by_id(self, property_id: int):
        return self.db.get(Property, property_id)

    def list_by_user(self, user_id: int) -> list[Property]:
        return self.db.query(Property).filter(Property.user_id == user_id).all()

    def get_by_id_and_user(self, property_id: int, user_id: int):
        return (
            self.db.query(Property)
            .filter(Property.id == property_id, Property.user_id == user_id)
            .first()
        )

    def exists_by_nome(self, user_id: int, nome: str):
        return (
            self.db.query(Property)
            .filter(Property.user_id == user_id, Property.name == nome)
            .first()
            is not None
        )

    def counter_by_user(self, user_id: int):
        return self.db.query(Property).filter(Property.user_id == user_id).count()
