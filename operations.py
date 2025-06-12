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
def listar_professores():
    for professor in Professor.select():
        print(f"{professor.id}: {professor.nome} ({professor.email})")

@db_session
def listar_professores_com_retorno():
    return list(Professor.select())

@db_session
def listar_disciplinas_com_retorno():
    return list(Disciplina.select())

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

@db_session
def add_disciplinas_batch(arquivo):
    from utils import ler_csv
    df = ler_csv(arquivo)

    for _, row in df.iterrows():
        try:
            Disciplina(
                nome=row['nome'],
                creditos=int(row['creditos']),
                ementa=row.get('ementa')
            )
            print(f"Disciplina {row['nome']} adicionada com sucesso.")
        except Exception as e:
            print(f"Erro ao adicionar disciplina {row.get('nome', 'desconhecida')}: {e}")

@db_session
def add_turmas_batch(arquivo):
    from utils import ler_csv 
    df = ler_csv(arquivo)

    for _, row in df.iterrows():
        disciplina = Disciplina.get(id=row['id_disciplina'])
        professor = Professor.get(id=row['id_professor'])
        if disciplina and professor:
            Turma(nome=row['nome'], disciplina=disciplina, professor=professor)
            print(f"Turma {row['nome']} adicionada com sucesso.")
        else:
            print(f"Erro: Disciplina ou professor não encontrado para turma {row['nome']}.")
@db_session
def add_frequencias_batch(arquivo):
    from utils import ler_csv
    df = ler_csv(arquivo)

    for _, row in df.iterrows():
        try:
            data = datetime.strptime(row['data'], "%Y-%m-%d").date()
            aluno = Aluno.get(id=row['id_aluno'])
            turma = Turma.get(id=row['id_turma'])
            if aluno and turma:
                Frequencia(aluno=aluno, turma=turma, data=data, presente=row['presente'])
                print(f"Frequência adicionada para {aluno.nome} na turma {turma.nome}.")
            else:
                print(f"Erro: Aluno ou turma não encontrado para frequência em {data}.")
        except Exception as e:
            print(f"Erro ao adicionar frequência: {e}")
@db_session
def add_notas_batch(arquivo):
    from utils import ler_csv
    df = ler_csv(arquivo)

    for _, row in df.iterrows():
        try: 
            aluno = Aluno.get(id=row['id_aluno'])
            turma = Turma.get(id=row['id_turma'])
            if aluno and turma:
                Nota(aluno=aluno, turma=turma, nota=row['nota'])
                print(f"Nota adicionada para {aluno.nome} na turma {turma.nome}.")
            else:
                print(f"Erro: Aluno ou turma não encontrado para nota.")
        except Exception as e:
            print(f"Erro ao adicionar nota: {e}")
@db_session
def add_turmasAlunos_batch(arquivo):
    from utils import ler_csv
    df = ler_csv(arquivo)

    for _, row in df.iterrows():
        try:
            aluno = Aluno.get(id=row['id_aluno'])
            turma = Turma.get(id=row['id_turma'])
            if aluno and turma:
                TurmaAluno(aluno=aluno, turma=turma)
                print(f"Aluno {aluno.nome} vinculado à turma {turma.nome} com sucesso.")
            else:
                print(f"Erro: Aluno ou turma não encontrado para vinculação.")
        except Exception as e:
            print(f"Erro ao vincular aluno à turma: {e}")