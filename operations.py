from pony.orm import db_session
from models import *

@db_session
def add_professor(nome, email):
    Professor(nome=nome, email=email)

@db_session
def add_aluno(nome, matricula):
    Aluno(nome=nome, matricula=matricula)

@db_session
def listar_alunos():
    for aluno in Aluno.select():
        print(f"{aluno.id}: {aluno.nome} ({aluno.matricula})")

@db_session
def add_professores_batch(arquivo):
    from utils import ler_csv
    df = ler_csv(arquivo)
    for _, row in df.iterrows():
        Professor(nome=row['nome'], email=row['email'])
