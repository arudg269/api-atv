# Dentro de app/routers/health.py

@router.get("/me", response_model=User)
def read_me():
    return {
        "username": "douglas oliveira da silva 37022882",
        "email": "37022882@sempreunijuazeiro.com.br",
        "full_name": "douglas o da silva"
    }