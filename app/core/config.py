import os

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Database:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///banco_test.db")

        self.engine = create_engine(
            self.database_url, connect_args=self._get_connect_args()
        )

        self.base = Base

        if self.database_url.startswith("sqlite"):

            @event.listens_for(Engine, "connect")
            def set_sqlite_pragma(dbapi_connection, connection_record):
                cursor = dbapi_connection.cursor()
                cursor.execute("PRAGMA foreign_keys=ON")
                cursor.close()

        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def _get_connect_args(self):

        # sqlite
        if self.database_url.startswith("sqlite"):
            return {"check_same_thread": False}
        return {}


db = Database()
engine = db.engine


def get_db():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()
