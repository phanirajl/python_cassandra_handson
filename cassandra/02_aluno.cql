CREATE TABLE aluno
(
    id INT,
    nome VARCHAR,
    telefone INT,
    email VARCHAR,
    cidade_est VARCHAR,
    curso_matriculado_atual VARCHAR,
    turma VARCHAR,
    dt_inicio TIMESTAMP,
    dt_conclusao_prevista TIMESTAMP,
    PRIMARY KEY ( id )
) ;

CREATE INDEX aluno_nome_idx ON universidade.aluno (nome);
