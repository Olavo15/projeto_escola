# 🎓 Sistema Escolar CLI (Projeto Acadêmico)

Este projeto é um **Sistema de Gerenciamento Escolar em Linha de Comando (CLI)** desenvolvido como parte de um trabalho acadêmico na faculdade. 

## 📌 Objetivo

Desenvolver uma aplicação simples utilizando **Python**, **Pony ORM**, **argparse** e **SQLite**, que permita gerenciar professores, alunos, disciplinas, turmas, notas e frequência escolar por meio da linha de comando.

## 🚀 Funcionalidades

- ✅ Cadastrar professores individualmente
- ✅ Cadastrar alunos individualmente
- ✅ Importar professores em lote via arquivo `.csv`
- ✅ Listar todos os alunos cadastrados
- 🛠️ (Planejado) Cadastro de turmas, notas e frequência


## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Pony ORM
- SQLite
- argparse
- pandas (para leitura de arquivos CSV)

## 🗂️ Estrutura de Pastas

projeto_escola/
├── db.py # Conexão com SQLite
├── models.py # Definições do banco (ORM)
├── operations.py # Funções de cadastro/listagem
├── main.py # Entrada do sistema (CLI)
├── utils.py # Leitura de CSV
├── professores.csv # Exemplo de entrada em lote
├── .gitignore # Arquivos ignorados
└── README.md # Este arquivo

## 🚀 Como usar

### 1. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate        
venv\Scripts\activate          


## ⚠️ Aviso

> Este sistema é **exclusivamente educacional**, **sem fins comerciais ou de produção**. Foi criado para fins de **aprendizado e avaliação universitária**.