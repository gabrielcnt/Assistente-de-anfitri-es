import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import Base
from app.models.agent import Agent
from app.models.user import User

# banco na memória
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

test_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    session = test_session_local()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def agente(db):
    agente = Agent(
        nome="Agente_teste",
        numero_whatsapp="21968766766",
        nivel_proatividade="baixo",
        usar_emojis=True,
    )
    db.add(agente)
    db.commit()
    db.refresh(agente)
    return agente


@pytest.fixture(scope="function")
def user(db):
    user = User(username="user teste", email="user1@email.com", password="12345")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
