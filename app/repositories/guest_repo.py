from app.models.guest import Guest
from app.repositories.base_repo import BaseRepository


class GuestRepository(BaseRepository):
    def get_by_id(self, guest_id: int):
        return self.db.get(Guest, guest_id)

    def get_by_phone_and_property(self, phone: str, property_id: int):
        return (
            self.db.query(Guest)
            .filter(Guest.cell_phone_number == phone, Guest.property_id == property_id)
            .first()
        )

    def list_by_imovel(self, property_id: int) -> list[Guest]:
        return self.db.query(Guest).filter(Guest.property_id == property_id).all()
