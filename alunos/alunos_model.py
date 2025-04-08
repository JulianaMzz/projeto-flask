dados = {
    "alunos": [
        {"id": 1, "nome": "Renata", "idade": 19, "turma_id": 1, "data_nascimento": "2007-01-01", "nota_1_semestre": 8.5, "nota_2_semestre": 7.5, "media": 8.0},
    ]
}

def listar_alunos():
    return dados["alunos"]

def aluno_por_id(id_aluno):
    aluno = next((a for a in dados["alunos"] if a["id"] == id_aluno), None)
    if aluno is None:
        raise ValueError("Aluno não encontrado")
    return aluno

def adicionar_aluno(aluno):
    dados["alunos"].append(aluno)

def atualizar_aluno(id_aluno, novos_dados):
    aluno = aluno_por_id(id_aluno)
    aluno.update(novos_dados)

def excluir_aluno(id_aluno):
    aluno = aluno_por_id(id_aluno)
    dados["alunos"].remove(aluno)