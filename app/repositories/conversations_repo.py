from app.models.conversations import Conversations
from app.repositories.base_repo import BaseRepository


class ConversationRepository(BaseRepository):
    def get_by_id(self, conversation_id: int):
        return self.db.get(Conversations, conversation_id).first()

    def get_conversation_active(self, property_id: int, guest_id: int):
        return (
            self.db.query(Conversations)
            .filter(
                Conversations.property_id == property_id,
                Conversations.guest_id == guest_id,
                Conversations.status != "encerrada",
            )
            .all()
        )

    def list_by_id_property(self, property_id: int):
        return (
            self.db.query(Conversations)
            .filter(Conversations.property_id == property_id)
            .all()
        )
