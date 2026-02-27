import app.models

from app.core.config import Base, engine


def init_db():
    Base.metadata.create_all(bind=engine)