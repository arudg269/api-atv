from fastapi import FastAPI
from .routers import health
from .core.config import settings

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION
)

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}

