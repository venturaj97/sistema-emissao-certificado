from pydantic import BaseModel, EmailStr
from datetime import date
from uuid import UUID


class Aluno(BaseModel):
    nome: str
    cpf: UUID
    matricula: UUID
    email: EmailStr
    media: float
    frequencia: float

class Curso(BaseModel):
    nome: str
    cargaHoraria: int
    notaMinima: float

class Secretaria(BaseModel):
    nomeResponsavel: str
    telefone: str

class Certificado(BaseModel):
    numero: UUID
    dataEmissao: date
    hashQRCode: str