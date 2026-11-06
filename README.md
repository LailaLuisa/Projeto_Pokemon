# PokeAPI - Pipeline de dados 👾
Pipeline de ETL desenvolvido em Python para extração de dados da primeira geração de pokemon da PokeAPI e persistência em banco de dados relacional PostgreSQL.

## 🚀 Objetivo do projeto:

O projeto executa um fluxo automatizado dividido em duas etapas principais:
1. *Coleta e Transformação:* Varre os IDs de 1 a 150 da PokeAPI utilizando tratamento de dados, controle de requisições (time.sleep) e filtros para extrair informações básicas (ID, nome, altura, peso, experiência e tipo principal). Os dados são estruturados e convertidos em um DataFrame com pandas.
2. *Carga (Load):* Conecta-se de forma segura a um banco de dados PostgreSQL utilizando variáveis de ambiente (.env) e carrega o DataFrame diretamente para uma tabela utilizando SQLAlchemy.

## 📁 Estrutura do Repositório

- *pipelines.py*: Contém a classe PokemonPipeline com os métodos de requisição, tratamento de erros e gravação no banco.
- *main.py*: Script de orquestração para instanciar a classe e rodar o pipeline.
- *consultas_db.ipynb*: Jupyter Notebook contendo queries SQL executadas via cursor para validar e consultar os dados persistidos no PostgreSQL.

## 🛠️ Tecnologias Utilizadas

- Linguagem de programação Python;
- Bibliotecas: Pandas, Requests, Dotenv, SQLAlchemy & Psycopg2;
- PostgreSQL;
- Jupyter Notebook.
