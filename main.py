import argparse
from operations import *

parser = argparse.ArgumentParser(description="Sistema Escolar CLI")
subparsers = parser.add_subparsers(dest="comando")

p1 = subparsers.add_parser("add-professor")
p1.add_argument("--nome", required=True)
p1.add_argument("--email", required=True)
p1.add_argument("--nascimento", required=False)
p1.add_argument("--especialidade", required=False)

p2 = subparsers.add_parser("add-aluno")
p2.add_argument("--nome", required=True)
p2.add_argument("--matricula", required=True)
p2.add_argument("--email", required=True)
p2.add_argument("--nascimento", required=True)

p3 = subparsers.add_parser("add-professores-batch")
p3.add_argument("--arquivo", required=True)

p4 = subparsers.add_parser("listar-alunos")


p5 = subparsers.add_parser("add-alunos-batch")
p5.add_argument("--arquivo", required=True)

p6 = subparsers.add_parser("add-nota")
p6.add_argument("--id-aluno", type=int, required=True)
p6.add_argument("--id-turma", type=int, required=True)
p6.add_argument("--valor", type=float, required=True)

p7 = subparsers.add_parser("add-disciplina")
p7.add_argument("--nome", required=True)
p7.add_argument("--creditos", type=int, required=True)
p7.add_argument("--ementa", required=False)

p8 = subparsers.add_parser("add-turma")
p8.add_argument("--nome", required=True)
p8.add_argument("--id-disciplina", type=int, required=True)
p8.add_argument("--id-professor", type=int, required=True)

p9 = subparsers.add_parser("add-turma-aluno")
p9.add_argument("--id-aluno", type=int, required=True)
p9.add_argument("--id-turma", type=int, required=True)

p10 = subparsers.add_parser("add-frequencia")
p10.add_argument("--id-aluno", type=int, required=True)
p10.add_argument("--id-turma", type=int, required=True)
p10.add_argument("--data", required=True)
p10.add_argument("--presente", type=bool, required=True)

p11 = subparsers.add_parser("add-disciplinas-batch")
p11.add_argument("--arquivo", required=True)

p12 = subparsers.add_parser("add-turmas-batch")
p12.add_argument("--arquivo", required=True)

p13 = subparsers.add_parser("add-frequencias-batch")
p13.add_argument("--arquivo", required=True)

p14 = subparsers.add_parser("add-notas-batch")
p14.add_argument("--arquivo", required=True)

p15 = subparsers.add_parser("add-turmasAlunos-batch")
p15.add_argument("--arquivo", required=True)

p16 = subparsers.add_parser("listar-professores")

p17 = subparsers.add_parser("criar-turma-interativo")

p18 = subparsers.add_parser("selecionar-professor")


args = parser.parse_args()

if args.comando == "add-professor":
    add_professor(args.nome, args.email, args.nascimento, args.especialidade)
elif args.comando == "add-aluno":
    add_aluno(args.nome, args.matricula, args.email, args.nascimento)
elif args.comando == "add-professores-batch":
    add_professores_batch(args.arquivo)
elif args.comando == "add-alunos-batch":
    add_alunos_batch(args.arquivo)
elif args.comando == "listar-alunos":
    listar_alunos()
elif args.comando == "add-nota":
    add_nota(args.id_aluno, args.id_turma, args.valor)
    print("Nota adicionada com sucesso.")
elif args.comando == "add-disciplina":
    add_disciplina(args.nome, args.creditos, args.ementa)
    print("Disciplina adicionada com sucesso.")
elif args.comando == "add-turma":
    add_turma(args.nome, args.id_disciplina, args.id_professor)
    print("Turma adicionada com sucesso.")
elif args.comando == "add-turma-aluno":
    add_turma_aluno(args.id_aluno, args.id_turma)
    print("Aluno vinculado à turma com sucesso.")
elif args.comando == "add-frequencia":
    add_frequencia(args.id_aluno, args.id_turma, args.data, args.presente)
    print("Frequência adicionada com sucesso.")
elif args.comando == "add-disciplinas-batch":
    add_disciplinas_batch(args.arquivo)
elif args.comando == "add-turmas-batch":
    add_turmas_batch(args.arquivo)
elif args.comando == "add-frequencias-batch":
    add_frequencias_batch(args.arquivo)
elif args.comando == "add-notas-batch":
    add_notas_batch(args.arquivo)
elif args.comando == "add-turmasAlunos-batch":
    add_turmasAlunos_batch(args.arquivo)
elif args.comando == "listar-professores":
    listar_professores()
elif args.comando == "criar-turma-interativo":
    from operations import listar_professores_com_retorno, listar_disciplinas_com_retorno

    print("\n=== Disciplinas Disponíveis ===")
    disciplinas = listar_disciplinas_com_retorno()
    for disc in disciplinas:
        print(f"{disc.id}: {disc.nome} ({disc.creditos} créditos)")
    
    id_disciplina = int(input("Digite o ID da disciplina: "))

    print("\n=== Professores Disponíveis ===")
    professores = listar_professores_com_retorno()
    for prof in professores:
        print(f"{prof.id}: {prof.nome} ({prof.email})")

    id_professor = int(input("Digite o ID do professor: "))
    nome_turma = input("Digite o nome da turma: ")

    add_turma(nome_turma, id_disciplina, id_professor)
    print("Turma criada com sucesso.")
elif args.comando == "selecionar-professor":
    from operations import listar_professores_com_retorno
    professores = listar_professores_com_retorno()
    
    print("\n=== Lista de Professores ===")
    for prof in professores:
        print(f"{prof.id}: {prof.nome} ({prof.email})")

    try:
        id_escolhido = int(input("\nDigite o ID do professor que deseja selecionar: "))
        professor = next((p for p in professores if p.id == id_escolhido), None)
        
        if professor:
            print(f"\n✅ Professor selecionado: {professor.nome} ({professor.email})")
        else:
            print("❌ ID inválido. Professor não encontrado.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")