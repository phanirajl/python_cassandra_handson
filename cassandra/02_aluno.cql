CREATE TABLE aluno
(
    id INT,
    nome VARCHAR,
    telefone INT,
    email VARCHAR,
    cidade_est VARCHAR,
    curso_matriculado_atual VARCHAR,
    turma VARCHAR,
    dt_inicio VARCHAR,
    dt_conclusao_prevista VARCHAR,
    PRIMARY KEY ( id )
) ;

CREATE INDEX aluno_nome_idx ON universidade.aluno (nome);
