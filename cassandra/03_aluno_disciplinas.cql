CREATE TABLE aluno_disciplina
(
    disciplina VARCHAR,
    ano_disciplina VARCHAR,
    id_prof INT,
    prof_resp VARCHAR,
    curso_disciplina VARCHAR,
    id_aluno INT,
    nome_aluno VARCHAR,
    curso_aluno VARCHAR,
    dt_matricula_aluno TIMESTAMP,
    status_aluno_disciplina VARCHAR,
    PRIMARY KEY ( disciplina, ano_disciplina)
) ;

CREATE INDEX universidade_nome_aluno_idx ON universidade.aluno_disciplina (nome_aluno);
CREATE INDEX universidade_prof_resp_idx ON universidade.aluno_disciplina (prof_resp);
