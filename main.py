from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.util.config import DB_URL
from app.util.database import init_db
from app.util.init_models import init_models
from app.util.log import LoggingMiddleware
from app.util.root_router import router as root_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)
app.add_middleware(LoggingMiddleware)
app.include_router(root_router)


@app.on_event("startup")
async def on_startup():
    await init_db()
    init_models()


@app.get(path="/")
async def home():
    return {"message": "Hello, World!"}
