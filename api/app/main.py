from fastapi import FastAPI
from .routers import health

app = FastAPI(
    title="Minha API",
    description="API com rotas separadas.",
    version="1.0.0"
)

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}

