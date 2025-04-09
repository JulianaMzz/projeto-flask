dados = {
    "alunos": [
        {
            "id": 1,
            "nome": "Renata",
            "idade": 19,
            "turma_id": 1,
            "data_nascimento": "2007-01-01",
            "nota_1_semestre": 8.5,
            "nota_2_semestre": 7.5,
            "media_final": 8.0
        },
    ]
}

def listar_alunos():
    return dados["alunos"]

def aluno_por_id(id_aluno):
    aluno = next((a for a in dados["alunos"] if a["id"] == id_aluno), None)
    if aluno is None:
        raise ValueError("Aluno não encontrado")
    return aluno

def calcular_media(nota1, nota2):
    return round((nota1 + nota2) / 2, 2)

def adicionar_aluno(aluno):
    if any(a["id"] == aluno["id"] for a in dados["alunos"]):
        raise ValueError("Já existe um aluno com esse ID")
    
 
    if "nota_1_semestre" in aluno and "nota_2_semestre" in aluno:
        aluno["media_final"] = calcular_media(aluno["nota_1_semestre"], aluno["nota_2_semestre"])
    
    dados["alunos"].append(aluno)

def atualizar_aluno(id_aluno, novos_dados):
    aluno = aluno_por_id(id_aluno)
    aluno.update(novos_dados)
    
    if "nota_1_semestre" in novos_dados or "nota_2_semestre" in novos_dados:
        nota1 = aluno.get("nota_1_semestre", 0)
        nota2 = aluno.get("nota_2_semestre", 0)
        aluno["media_final"] = calcular_media(nota1, nota2)

def excluir_aluno(id_aluno):
    aluno = aluno_por_id(id_aluno)
    dados["alunos"].remove(aluno)