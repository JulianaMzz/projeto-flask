# School System - Flask API

Este repositório contém uma aplicação web desenvolvida com Flask, voltada para o gerenciamento de dados escolares. A API fornece recursos para administrar informações de alunos, professores e turmas, permitindo operações completas de criação, leitura, atualização e exclusão (CRUD).

## Visão Geral

A aplicação foi construída com uma abordagem modular, utilizando Blueprints para organizar as rotas de cada entidade. A base de dados utilizada nesta versão é SQLite, com planejamento futuro para adoção do MySQL.

## Funcionalidades da API

As seguintes operações estão disponíveis para cada uma das entidades:

- Inserção de novos registros
- Consulta de todos os registros
- Consulta de registros por ID
- Atualização de dados existentes
- Remoção de registros

## Estrutura do Projeto

O projeto está organizado em pastas separadas por responsabilidade:

projeto-flask-main/
├── alunos/ # Rotas e lógica dos alunos

├── professores/ # Funcionalidade dos professores

├── turmas/ # Gerenciamento das turmas

├── app.py # Ponto de entrada da aplicação

├── config.py # Configurações gerais

├── init_db.py # Inicialização do banco

├── requirements.txt # Dependências do projeto

├── Dockerfile # Configuração para build com Docker

└── docker-compose.yml


## Tecnologias

- Python 3 e Flask
- SQLite
- Docker
- Flask-RESTX (estrutura para documentação)
- Testes com unittest e pytest

## Executando com Docker

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/projeto-flask-main.git
cd projeto-flask-main



## Integração com outros microsserviços
Este sistema foi integrado com os microsserviços de Rservas e Atividades.
Para Facilitar a execução conjunta dos serviços, foi criado um repositório de integração opcional com 'docker-compose':
https://github.com/JulianaMzz/Integracao-microsservicos.git - Repositório de Integração de Microsserviços.
