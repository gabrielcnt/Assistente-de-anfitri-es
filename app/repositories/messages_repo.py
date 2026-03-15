from sqlalchemy import func

from app.models.messages import Message
from app.repositories.base_repo import BaseRepository


class MessageRepository(BaseRepository):
    def get_by_id(self, message_id: int):
        return self.db.get(Message, message_id)

    def get_by_external_message_id(self, external_message_id: str):
        return (
            self.db.query(Message)
            .filter(Message.external_message_id == external_message_id)
            .first()
        )

    def list_by_conversation(self, conversation_id: int):
        return (
            self.db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.asc())
            .all()
        )

    def search_latest_messages(self, conversation_id: int, limit: int = 10):
        return (
            self.db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.desc())
            .limit(limit)
            .all()
        )

    def count_by_messages(self, conversation_id: int):
        return (
            self.db.query(func.count(Message.id))
            .filter(Message.conversation_id == conversation_id)
            .scalar()
        )

    def messages_role(self, conversation_id: int, role: str):
        return (
            self.db.query(Message)
            .filter(Message.conversation_id == conversation_id, Message.role == role)
            .all()
        )
