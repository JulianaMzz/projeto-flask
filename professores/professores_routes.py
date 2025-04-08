# professores_routes.py

from flask import Blueprint, request, jsonify
from .professores_model import (
    listar_professores,
    professor_por_id,
    adicionar_professor,
    atualizar_professor,
    excluir_professor
)

# Criando o blueprint para a rota de professores
professores_blueprint = Blueprint('professores', __name__)

# Rota para listar todos os professores
@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    """Rota para listar todos os professores."""
    return jsonify(listar_professores())

# Rota para obter um professor pelo ID
@professores_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    """Rota para obter um professor pelo ID."""
    try:
        professor = professor_por_id(id_professor)
        return jsonify(professor)
    except ValueError:
        return jsonify({'error': 'Professor não encontrado'}), 404

# Rota para criar um novo professor
@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    """Rota para criar um novo professor."""
    dados = request.json
    if not dados or 'nome' not in dados or 'idade' not in dados or 'materia' not in dados:
        return jsonify({"error": "Nome, idade e matéria são obrigatórios"}), 400

    novo_professor = {
        "id": len(listar_professores()) + 1,
        "nome": dados["nome"],
        "idade": dados["idade"],
        "materia": dados["materia"],
        "observacoes": dados.get("observacoes", "")
    }

    adicionar_professor(novo_professor)
    return jsonify(novo_professor), 201

# Rota para atualizar um professor existente
@professores_blueprint.route('/professores/<int:id_professor>', methods=['PUT'])
def update_professor(id_professor):
    """Rota para atualizar um professor existente."""
    dados = request.json
    try:
        atualizar_professor(id_professor, dados)
        return jsonify(professor_por_id(id_professor))
    except ValueError:
        return jsonify({'error': 'Professor não encontrado'}), 404

# Rota para deletar um professor pelo ID
@professores_blueprint.route('/professores/<int:id_professor>', methods=['DELETE'])
def delete_professor(id_professor):
    """Rota para deletar um professor pelo ID."""
    try:
        excluir_professor(id_professor)
        return jsonify({"message": "Professor removido com sucesso"}), 200
    except ValueError:
        return jsonify({'error': 'Professor não encontrado'}), 404
