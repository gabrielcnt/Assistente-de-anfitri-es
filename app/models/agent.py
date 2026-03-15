from sqlalchemy import Boolean, Column, Integer, String, Text

from app.core.config import db


class Agent(db.base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True)

    nome = Column(String, nullable=True)
    personality_text = Column(Text, nullable=True)
    tone_of_voice = Column(String, nullable=True)
    welcome_message = Column(Text, nullable=True)

    whatapp_number = Column(String, nullable=False)

    level_proactivity = Column(String, nullable=False)
    user_emojis = Column(Boolean, nullable=False)
    default_language = Column(String, nullable=True, default="pt-br")

    warnings = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)

    def disable(self):
        self.is_active = False
