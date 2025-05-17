from app.models import Aluno

from fastapi import APIRouter

router = APIRouter()

ALUNOS = [
    {
        "aluno_id": 1,
        "nome": "Joao",
        "cpf": "teste",
        "email": "email",
        "media": 9.0,
        "frequencia": 75.0
    },
    {
        "aluno_id": 2,
        "nome": "Joao2",
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

@router.get("/aluno/{aluno_id}", tags=["Alunos"])
def buscar_aluno(aluno_id: int):
    return {"aluno_id": aluno_id}