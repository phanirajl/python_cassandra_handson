from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns, ValidationError
from marshmallow import Schema, fields
from config import carrega_sessao


class AlunoModel(Model):
    '''
    Classe responsável por realizar a interação com a base de dados.
    '''
    __table_name__ = "aluno"
    connection.set_session(carrega_sessao())

    id = columns.Integer(primary_key=True)
    nome = columns.Text(index=True, required=True)
    telefone = columns.Integer(required=True)
    email = columns.Text(required=True)
    cidade_est  = columns.Text(required=True)
    curso_matriculado_atual  = columns.Text(required=True)
    turma  = columns.Text(required=True)
    dt_inicio = columns.DateTime(required=True)
    dt_conclusao_prevista = columns.DateTime(required=True)


class AlunoSchema(Schema):
    '''
    Classe responsável por realizar a serialização da classe para um objeto JSON.
    '''
    id = fields.Str()
    nome = fields.Str()
    telefone = fields.Str()
    email = fields.Str()
    cidade_est = fields.Str()
    curso_matriculado_atual = fields.Str()
    turma = fields.Str()
    dt_inicio = fields.Str()
    dt_conclusao_prevista = fields.Str()
