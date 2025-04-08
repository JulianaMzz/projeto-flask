# turmas_model.py

# Simulação de banco de dados em memória (lista de dicionários)
dados = {
    "turmas": [
        {"id": 1, "descricao": "6º ano A", "professor_id": 1, "ativo": True}
    ]
}

# Função para listar todas as turmas
def listar_turmas():
    """Retorna todas as turmas cadastradas."""
    return dados["turmas"]

# Função para obter uma turma pelo ID
def turma_por_id(id_turma):
    """Retorna uma turma pelo ID ou lança exceção se não encontrado."""
    turma = next((t for t in dados["turmas"] if t["id"] == id_turma), None)
    if turma is None:
        raise ValueError("Turma não encontrada")
    return turma

# Função para adicionar uma nova turma
def adicionar_turma(turma):
    """Adiciona uma nova turma."""
    dados["turmas"].append(turma)

# Função para atualizar os dados de uma turma
def atualizar_turma(id_turma, novos_dados):
    """Atualiza os dados de uma turma existente."""
    turma = turma_por_id(id_turma)
    turma.update(novos_dados)

# Função para excluir uma turma
def excluir_turma(id_turma):
    """Remove uma turma pelo ID."""
    turma = turma_por_id(id_turma)
    dados["turmas"].remove(turma)
