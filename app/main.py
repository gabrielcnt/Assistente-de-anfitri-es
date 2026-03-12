from fastapi import FastAPI

from app.api import imovel_router
from app.api import dicas_lugares_router
from app.api import auth_router

from dotenv import load_dotenv

from contextlib import asynccontextmanager

from app.core.seed_admin import seed_user

from app.core.config import db
from app.core.init_db import init_db

load_dotenv()

#importação do agente

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    session = db.SessionLocal()
    try:
        seed_user(session)
    finally:
        session.close()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(imovel_router.router)
app.include_router(dicas_lugares_router.router)
app.include_router(auth_router.router)

@app.get('/health')
def health():
    return {"status": "ok"}
