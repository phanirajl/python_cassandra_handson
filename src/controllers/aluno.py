from models.aluno import AlunoModel, AlunoSchema

class AlunoController():
    def __init__(self, id=None, nome=None, telefone=None, email=None,
        cidade_est=None, curso_matriculado_atual=None, turma=None,
        dt_inicio=None, dt_conclusao_prevista=None):
        self.id=id,
        self.nome=nome,
        self.telefone=telefone,
        self.email=email,
        self.cidade_est=cidade_est,
        self.curso_matriculado_atual=curso_matriculado_atual,
        self.turma=turma,
        self.dt_inicio=dt_inicio,
        self.dt_conclusao_prevista=dt_conclusao_prevista

    def listar(self):
        '''
        Lista os alunos.
        :param self: Palavra reservada em Python.
        :return: retorna o objeto JSON com a lista dos alunos.
        '''
        emails = AlunoModel()
        rows = emails.objects.all()

        schema = AlunoSchema(many=True)
        result = schema.dump(rows)

        return result

    def atualizar(self):
        '''
        Grava o aluno na base de dados.
        :param self: Palavra reservada em Python.
        :return: retorna o objeto JSON do aluno gravado no Banco.
        '''
        aluno = AlunoModel()

        row = aluno.create(id=self.id[0], nome=''.join(self.nome),
                           telefone=self.telefone[0], email=''.join(self.email),
                           cidade_est=''.join(self.cidade_est),
                           curso_matriculado_atual=''.join(self.curso_matriculado_atual),
                           turma=''.join(self.turma),
                           dt_inicio=''.join(self.dt_inicio),
                           dt_conclusao_prevista=''.join(self.dt_conclusao_prevista)
                           )

        schema = AlunoSchema()
        result = schema.dump(row)

        return result
