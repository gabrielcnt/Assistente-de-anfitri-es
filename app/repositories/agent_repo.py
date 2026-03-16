from app.models.agent import Agent
from app.repositories.base_repo import BaseRepository


class AgentRepository(BaseRepository):
    def get(self):
        return self.db.query(Agent).first()
