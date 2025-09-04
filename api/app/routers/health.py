from fastapi import APIRouter, BaseModel

# ESTA LINHA ESTAVA FALTANDO!
# Ela cria a variável 'router' que será usada para definir os endpoints.
router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None

@router.get("/health")
def read_health():
    return {"status": "ok"}

@router.get("/me", response_model=User)
def read_me():
    return {
        "username": "douglas oliveira da silva 37022882",
        "email": "37022882@sempreunijuazeiro.com.br",
        "full_name": "douglas o da silva"
    }

