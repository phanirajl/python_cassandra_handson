# python_cassandra_handson
Exemplo de criação de projeto utilizando Python e Cassandra

## Finalidade do projeto
Este projeto visa ser um Hands-on de um projeto para uma Universidade empregando a linguagem de programação Python e o  Banco de Dados NoSQL Cassandra.

## Como utilizar o projeto

### Cassandra

É necessário que o cassandra 3.11 ou superior esteja acessível.
Para criar a estrutura de dados necessária para rodar o projeto abre o console `cqlsh` e execute os comandos
presentes na pasta `./cassandra` seguindo a ordem da numeração.

1. 01_create_keyspace.sql
2. 02_aluno.cql
3. 03_aluno_disciplinas.cql
4. 04_carga_banco.cql

Após a criação da estrutura no cassandra, siga as instruções para instalar as dependências python.

### Python

É necessária que o python 3.6 ou superior esteja instalado.
Para configurar o ambiente clone este repositório e execute os comandos abaixo:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Após a instalação das dependências do projeto é só executá-lo com o comando abaixo:

```bash
python src/run.py
```

Para consultar a documentação dos endpoints da API basta acessar http://0.0.0.0:8088/apidocs
