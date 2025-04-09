from flask import Blueprint, jsonify, request
from alunos.alunos_model import (
    listar_alunos,
    aluno_por_id,
    adicionar_aluno,
    atualizar_aluno,
    excluir_aluno
)

alunos_routes = Blueprint('alunos_routes', __name__)


@alunos_routes.route('/alunos', methods=['GET'])
def rota_listar_alunos():
    return jsonify(listar_alunos())


@alunos_routes.route('/alunos/<int:id_aluno>', methods=['GET'])
def rota_aluno_por_id(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404

@alunos_routes.route('/alunos', methods=['POST'])
def rota_adicionar_aluno():
    novo_aluno = request.get_json()

    if not novo_aluno:
        return jsonify({'erro': 'Dados do aluno não fornecidos'}), 400

    try:
        adicionar_aluno(novo_aluno)
        return jsonify({'mensagem': 'Aluno adicionado com sucesso'}), 201
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 400


@alunos_routes.route('/alunos/<int:id_aluno>', methods=['PUT'])
def rota_atualizar_aluno(id_aluno):
    novos_dados = request.get_json()

    if not novos_dados:
        return jsonify({'erro': 'Dados para atualização não fornecidos'}), 400

    try:
        atualizar_aluno(id_aluno, novos_dados)
        return jsonify({'mensagem': 'Aluno atualizado com sucesso'})
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404

@alunos_routes.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def rota_excluir_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return jsonify({'mensagem': 'Aluno excluído com sucesso'})
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404