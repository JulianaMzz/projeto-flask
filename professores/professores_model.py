dados = {
    "professores": [
        {"id": 1, "nome": "Manoel", "idade": 23, "disciplina": "Português"},
    ]
}


def listar_professores():
    return dados["professores"]


def professor_por_id(id_professor):
    professor = next((p for p in dados["professores"] if p["id"] == id_professor), None)
    if professor is None:
        raise ValueError("Professor não foi encontrado")
    return professor


def adicionar_professor(professor):
    if not isinstance(professor, dict):
        raise ValueError("Formato inválido de professor")
    
    if any(p["id"] == professor["id"] for p in dados["professores"]):
        raise ValueError("Já existe um professor com esse id")
    
    dados["professores"].append(professor)


def atualizar_professor(id_professor, novos_dados):
    professor = professor_por_id(id_professor)
    professor.update(novos_dados)


def excluir_professor(id_professor):
    professor = professor_por_id(id_professor)
    dados["professores"].remove(professor)