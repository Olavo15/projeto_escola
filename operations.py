from pony.orm import db_session
from datetime import datetime
from models import *

@db_session
def add_professor(nome, email, nascimento, especialidade):
    Professor(nome=nome, email=email, nascimento=nascimento, especialidade=especialidade)

@db_session
def add_aluno(nome, matricula, email, nascimento):
    Aluno(nome=nome, matricula=matricula, email=email, nascimento=nascimento)

@db_session
def listar_alunos():
    for aluno in Aluno.select():
        print(f"{aluno.id}: {aluno.nome} ({aluno.matricula})")

@db_session
def add_professores_batch(arquivo):
    try:
        from utils import ler_csv
        df = ler_csv(arquivo)
    
        for _, row in df.iterrows():
            Professor(
                nome=row['nome'],
                email=row['email'],
                nascimento=row.get('nascimento'), 
                especialidade=row.get('especialidade')
            )
            print(f"Professor {row['nome']} adicionado com sucesso.")
    except Exception as e:
            print(f"Erro ao adicionar o professor {row.get('nome', 'desconhecido')}: {e}")

@db_session
def add_disciplina(nome, creditos, ementa=None):
    Disciplina(nome=nome, creditos=creditos, ementa=ementa)

@db_session
def add_turma(nome, id_disciplina, id_professor):
    disciplina = Disciplina.get(id=id_disciplina)
    professor = Professor.get(id=id_professor)
    if disciplina and professor:
        Turma(nome=nome, disciplina=disciplina, professor=professor)
    else:
        print("Disciplina ou professor não encontrado.")

@db_session
def add_turma_aluno(id_aluno, id_turma):
    aluno = Aluno.get(id=id_aluno)
    turma = Turma.get(id=id_turma)
    if aluno and turma:
        TurmaAluno(aluno=aluno, turma=turma)
    else:
        print("Aluno ou turma não encontrado.")

@db_session
def add_nota(id_aluno, id_turma, valor):
    aluno = Aluno.get(id=id_aluno)
    turma = Turma.get(id=id_turma)
    if aluno and turma:
        Nota(aluno=aluno, turma=turma, valor=valor)
    else:
        print("Aluno ou turma não encontrado.")

@db_session
def add_frequencia(id_aluno, id_turma, data, presente):
    aluno = Aluno.get(id=id_aluno)
    turma = Turma.get(id=id_turma)
    if aluno and turma:
        Frequencia(aluno=aluno, turma=turma, data=data, presente=presente)
    else:
        print("Aluno ou turma não encontrado.")
@db_session
def add_alunos_batch(arquivo):
    from utils import ler_csv
    df = ler_csv(arquivo)

    for _, row in df.iterrows():
        try:
            nascimento = datetime.strptime(row['nascimento'], "%Y-%m-%d").date()
            Aluno(
                nome=row['nome'],
                matricula=str(row['matricula']),
                email=row['email'],
                nascimento=nascimento
            )
            print(f"Aluno {row['nome']} adicionado com sucesso.")
        except Exception as e:
            print(f"Erro ao adicionar aluno {row.get('nome')}: {e}")
