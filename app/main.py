from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from app.api import admin_router, auth_router, places_tips_router, property_router, agent_router
from app.core.config import db
from app.core.init_db import init_db
from scripts.seed_admin import seed_user

load_dotenv()

# importação do agente


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
app.include_router(property_router.router)
app.include_router(places_tips_router.router)
app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(agent_router.router)


@app.get("/health")
def health():
    return {"status": "ok"}
