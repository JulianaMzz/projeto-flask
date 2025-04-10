dados = {
    "turmas": [
        {"id": 1, "nome": "1 ano B", "turno": "Manhã"},
    ]
}

def listar_turmas():
    return dados["turmas"]

def turma_por_id(id_turma):
    turma = next((t for t in dados["turmas"] if t["id"] == id_turma), None)
    if turma is None:
        raise ValueError("Turma não foi encontrada")
    return turma

def adicionar_turma(turma):
    if any(t['id'] == turma["id"] for t in dados["turmas"]):
        raise ValueError("Já existe uma turma com esse ID")
    dados["turmas"].append(turma)

def atualizar_turma(id_turma, novos_dados):
    turma = turma_por_id(id_turma)
    turma.update(novos_dados)

def excluir_turma(id_turma):
    turma = turma_por_id(id_turma)
    dados["turmas"].remove(turma)
