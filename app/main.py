from fastapi import FastAPI

from dotenv import load_dotenv

from contextlib import asynccontextmanager

from app.core.config import db
from app.core.init_db import init_db

load_dotenv()

#importação do agente

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/health')
def health():
    return {"status": "ok"}