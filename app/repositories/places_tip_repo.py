from app.models.places_tips import PlaceTip
from app.models.property import Property
from app.repositories.base_repo import BaseRepository


class PlacesTipRepository(BaseRepository):
    def create(self, property_id: int, dados) -> PlaceTip:
        data = dados.model_dump()

        if data.get("map_link"):
            data["map_link"] = str(data["map_link"])
        if data.get("tipo"):
            data["tipo"] = str(data["tipo"])
        tips = PlaceTip(property_id=property_id, **data)

        self.db.add(tips)
        return tips

    def get_by_id(self, places_tips_id: int):
        return self.db.get(PlaceTip, places_tips_id)

    def get_by_id_property_user(self, tips_id: int, property_id: int, user_id: int):
        return (
            self.db.query(PlaceTip)
            .join(Property)
            .filter(
                PlaceTip.id == tips_id,
                PlaceTip.property_id == property_id,
                Property.user_id == user_id,
            )
            .first()
        )

    # Listar dicas de lugares para um imovel
    def list_by_property(self, property_id: int) -> list[PlaceTip]:
        return self.db.query(PlaceTip).filter(PlaceTip.imovel_id == property_id).all()

    # Listar dicas de lugares para um imovel, filtrado por categoria
    def list_by_imovel_and_tipo(self, property_id: int, type: str) -> list[PlaceTip]:
        return (
            self.db.query(PlaceTip)
            .filter(PlaceTip.property_id == property_id, PlaceTip.type == type)
            .all()
        )

    # Verifica se uma dica com esse nome existe
    def exists_by_name(self, property_id: int, name: str) -> bool:
        return (
            self.db.query(PlaceTip.id)
            .filter(PlaceTip.property_id == property_id, PlaceTip.name == name)
            .first()
            is not None
        )
