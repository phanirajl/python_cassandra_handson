INSERT INTO aluno (
id,
nome ,
telefone,
email ,
cidade_est ,
curso_matriculado_atual ,
turma ,
dt_inicio ,
dt_conclusao_prevista
)
VALUES
(1, 'RODRIGO', 123456, 'RODRIGO@TESTE.COM', 'BARRETOS-SP', 'CIENCIA DA COMPUTACAO', 'TURMA 1', '2017-03-01', '2021-12-20');

INSERT INTO aluno (
id,
nome ,
telefone,
email ,
cidade_est ,
curso_matriculado_atual ,
turma ,
dt_inicio ,
dt_conclusao_prevista
)
VALUES
(2, 'TESTE', 987654321, 'TESTE@TESTE.COM', 'RIBEIRAO PRETO-SP', 'CIENCIA DA COMPUTACAO', 'TURMA 1', '2018-03-01', '2022-12-20');

INSERT INTO aluno_disciplina (
  disciplina ,
  ano_disciplina ,
  id_prof ,
  prof_resp ,
  curso_disciplina ,
  id_aluno ,
  nome_aluno ,
  curso_aluno ,
  dt_matricula_aluno ,
  status_aluno_disciplina
)
VALUES
('PROGRAMACAO WEB', '2019', 10, 'JOAO', 'CIENCIA DA COMPUTACAO', 1, 'RODRIGO', 'CIENCIA DA COMPUTACAO', '2019-02-01', 'CURSANDO');
