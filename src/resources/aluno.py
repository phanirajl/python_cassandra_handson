from flask import request
from flask_restful import Resource, abort
from controllers.aluno import AlunoController

class Aluno(Resource):
    '''
    Representação do Aluno
    '''
    def get(self):
        '''
        Busca Alunos.
        ---
        operationId: resources.aluno.get
        tags:
            - aluno
        description: Este procedimento realizada a leitura na tabela de aluno e os
                     retorna em um objeto JSON.
        response:
            200:
                schema:
                    properties:
                        id:
                            type: string
                        nome:
                            type: string
                        email:
                            type: string
                        cidade_est:
                            type: string
                        curso_matriculado_atual:
                            type: string
                        turma:
                            type: string
                        dt_inicio:
                            type: string
                        dt_conclusao_prevista:
                            type: string

        '''
        alunos = AlunoController()
        result = alunos.listar()

        if not result:
            abort(404, message="Nenhum registro encontrado na base de dados")

        return result

    def post(self):
        '''
        Insere um novo aluno.
        ---
        operationId: resources.aluno.post
        tags:
            - aluno
        description: Este procedimento recebe os dados do aluno através de um objeto JSON,
                     o qual é inserido no Banco de Dados Cassandra.
        parameters:
            - in: body
              name: aluno
              description: Dados do aluno a ser inserido.
              required: True
              schema:
                type: object
                properties:
                    id:
                        type: string
                        required: True
                        description: id do aluno a ser inserido.
                    nome:
                        type: string
                        required: True
                        description: Nome do aluno a ser inserido.
                    telefone:
                        type: string
                        required: True
                        description: Telefone do aluno a ser inserido.
                    email:
                        type: string
                        required: True
                        description: Email do aluno a ser inserido.
                    cidade_est:
                        type: string
                        required: True
                        description: Cidade-Estado do aluno a ser inserido. Por exemplo, Ribeirão Preto-SP.
                    curso_matriculado_atual:
                        type: string
                        required: True
                        description: Curso em que o aluno a ser inserido está matriculado atualmente.
                    turma:
                        type: string
                        required: True
                        description: Turma do aluno a ser inserido.
                    dt_inicio:
                        type: string
                        required: True
                        description: A Data de início do aluno a ser inserido.
                    dt_conclusao_prevista:
                        type: string
                        required: True
                        description: Previsão de conclusão do aluno a ser inserido. Aluno cursando Ciência da Computação tem previsão de concluir em 4 anos da Data de Início.

        '''
        data = request.get_json(force=True)
        id = data.get("id")
        nome = data.get("nome")
        telefone = data.get("telefone")
        email = data.get("email")
        cidade_est = data.get("cidade_est")
        curso_matriculado_atual = data.get("curso_matriculado_atual")
        turma = data.get("turma")
        dt_inicio = data.get("dt_inicio")
        dt_conclusao_prevista = data.get("dt_conclusao_prevista")

        aluno = AlunoController(id,nome,telefone,email,
        cidade_est,curso_matriculado_atual,turma,
        dt_inicio,dt_conclusao_prevista)

        result = aluno.atualizar()

        if not result:
            abort(406, message="Não foi possível atualizar o aluno")

        return result
