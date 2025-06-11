from pony.orm import Required, Optional, Set
from datetime import date
from db import db

class Professor(db.Entity):
    nome = Required(str)
    email = Required(str, unique=True)
    nascimento = Required(date)
    especialidade = Required(str)
    turmas = Set("Turma")

class Aluno(db.Entity):
    nome = Required(str)
    email = Required(str, unique=True)         
    nascimento = Required(date)                
    matricula = Required(str, unique=True)     
    turma_alunos = Set("TurmaAluno")
    notas = Set("Nota")
    frequencias = Set("Frequencia")

class Disciplina(db.Entity):
    nome = Required(str)
    creditos = Required(int)
    ementa = Optional(str)
    turmas = Set("Turma")

class Turma(db.Entity):
    nome = Required(str)
    disciplina = Required(Disciplina)
    professor = Required(Professor)
    turma_alunos = Set("TurmaAluno")
    notas = Set("Nota")
    frequencias = Set("Frequencia")

class TurmaAluno(db.Entity):
    aluno = Required(Aluno)
    turma = Required(Turma)

class Nota(db.Entity):
    aluno = Required(Aluno)
    turma = Required(Turma)
    nota = Required(int)

class Frequencia(db.Entity):
    aluno = Required(Aluno)
    turma = Required(Turma)
    data = Required(date)
    presente = Required(bool)

# Geração do mapeamento
db.generate_mapping(create_tables=True)
