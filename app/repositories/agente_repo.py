from app.repositories.base_repo import BaseRepository
from app.models.agente import Agente


class AgenteRepository(BaseRepository):
    

    def get(self):
        return (
            self.db.query(Agente).first()
        )