# professores_model.py

# Simulação de banco de dados em memória (lista de dicionários)
dados = {
    "professores": [
        {"id": 1, "nome": "Lucas", "idade": 40, "materia": "História", "observacoes": "Muito dedicado"}
    ]
}

# Função para listar todos os professores
def listar_professores():
    """Retorna todos os professores cadastrados."""
    return dados["professores"]

# Função para obter um professor pelo ID
def professor_por_id(id_professor):
    """Retorna um professor pelo ID ou lança exceção se não encontrado."""
    professor = next((p for p in dados["professores"] if p["id"] == id_professor), None)
    if professor is None:
        raise ValueError("Professor não encontrado")
    return professor

# Função para adicionar um novo professor
def adicionar_professor(professor):
    """Adiciona um novo professor."""
    dados["professores"].append(professor)

# Função para atualizar os dados de um professor
def atualizar_professor(id_professor, novos_dados):
    """Atualiza os dados de um professor existente."""
    professor = professor_por_id(id_professor)
    professor.update(novos_dados)

# Função para excluir um professor
def excluir_professor(id_professor):
    """Remove um professor pelo ID."""
    professor = professor_por_id(id_professor)
    dados["professores"].remove(professor)
