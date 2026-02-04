import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

class Database:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///./banco_test.db")

        self.engine = create_engine(
            self.database_url,
            connect_args=self._get_connect_args()
        )

        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

        self.base = declarative_base()

def _get_connect_args(self):

    #sqlite
    if self.database_url.startswith("sqlite"):
        return {"check_same_thread":False}
    return {}

db = Database()