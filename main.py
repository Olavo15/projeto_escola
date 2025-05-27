import argparse
from operations import *

parser = argparse.ArgumentParser(description="Sistema Escolar CLI")
subparsers = parser.add_subparsers(dest="comando")

p1 = subparsers.add_parser("add-professor")
p1.add_argument("--nome", required=True)
p1.add_argument("--email", required=True)

p2 = subparsers.add_parser("add-aluno")
p2.add_argument("--nome", required=True)
p2.add_argument("--matricula", required=True)

p3 = subparsers.add_parser("add-professores-batch")
p3.add_argument("--arquivo", required=True)

p4 = subparsers.add_parser("listar-alunos")

args = parser.parse_args()

if args.comando == "add-professor":
    add_professor(args.nome, args.email)
elif args.comando == "add-aluno":
    add_aluno(args.nome, args.matricula)
elif args.comando == "add-professores-batch":
    add_professores_batch(args.arquivo)
elif args.comando == "listar-alunos":
    listar_alunos()
