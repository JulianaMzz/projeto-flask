# alunos_routes.py

from flask import Blueprint, request, jsonify
from .alunos_model import (
    listar_alunos,
    aluno_por_id,
    adicionar_aluno,
    atualizar_aluno,
    excluir_aluno
)


alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    """Rota para listar todos os alunos."""
    return jsonify(listar_alunos())

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    """Rota para obter um aluno pelo ID."""
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except ValueError:
        return jsonify({'error': 'Aluno não encontrado'}), 404

@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    """Rota para criar um novo aluno."""
    dados = request.json
    if not dados or 'nome' not in dados or 'idade' not in dados or 'turma_id' not in dados:
        return jsonify({"error": "Nome, idade e turma_id são obrigatórios"}), 400

    novo_aluno = {
        "id": len(listar_alunos()) + 1,
        "nome": dados["nome"],
        "idade": dados["idade"],
        "turma_id": dados["turma_id"],
        "data_nascimento": dados.get("data_nascimento", ""),
        "nota_1_semestre": dados.get("nota_1_semestre", 0.0),
        "nota_2_semestre": dados.get("nota_2_semestre", 0.0),
        "media": (dados.get("nota_1_semestre", 0.0) + dados.get("nota_2_semestre", 0.0)) / 2
    }

    adicionar_aluno(novo_aluno)
    return jsonify(novo_aluno), 201

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_aluno(id_aluno):
    """Rota para atualizar um aluno existente."""
    dados = request.json
    try:
        atualizar_aluno(id_aluno, dados)
        return jsonify(aluno_por_id(id_aluno))
    except ValueError:
        return jsonify({'error': 'Aluno não encontrado'}), 404

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    """Rota para deletar um aluno pelo ID."""
    try:
        excluir_aluno(id_aluno)
        return jsonify({"message": "Aluno removido com sucesso"}), 200
    except ValueError:
        return jsonify({'error': 'Aluno não encontrado'}), 404
