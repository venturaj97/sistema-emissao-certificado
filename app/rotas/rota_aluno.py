from app.models import Aluno

from fastapi import APIRouter

router = APIRouter()

ALUNOS = [
    {
        "nome": "Joao",
        "matricula" ""
        "cpf": "teste",
        "email": "email",
        "media": 9.0,
        "frequencia": 75.0
    },
    {
        "nome": "Joao2",
        "matricula": "123456",
        "cpf": "teste2",
        "email": "email2",
        "media": 8.0,
        "frequencia": 85.0
    }
]

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.post("/aluno", tags=["Alunos"])
def create_item(aluno: Aluno):
    return aluno

@router.get("/aluno", tags=["Alunos"])
def listar_alunos() -> list:
    return ALUNOS