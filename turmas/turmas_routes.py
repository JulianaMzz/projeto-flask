from flask import Blueprint, jsonify, request
from turmas.turmas_model import listar_turmas, turma_por_id, adicionar_turma, atualizar_turma, excluir_turma

turmas_routes = Blueprint('turmas_routes', __name__)

@turmas_routes.route('/turmas', methods=['GET'])
def rota_listar_turmas():
    return jsonify(listar_turmas())

@turmas_routes.route('/turmas/<int:id_turma>', methods=['GET'])
def rota_turma_por_id(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return jsonify(turma)
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404

@turmas_routes.route('/turmas', methods=['POST'])
def rota_adicionar_turma():
    nova_turma = request.get_json()
    adicionar_turma(nova_turma)
    return jsonify(nova_turma), 201  

@turmas_routes.route('/turmas/<int:id_turma>', methods=['PUT'])
def rota_atualizar_turma(id_turma):
    novos_dados = request.get_json()
    try:
        atualizar_turma(id_turma, novos_dados)
        return jsonify({'mensagem': 'Turma atualizada com sucesso'})
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404

@turmas_routes.route('/turmas/<int:id_turma>', methods=['DELETE'])
def rota_excluir_turma(id_turma):
    try:
        excluir_turma(id_turma)
        return jsonify({'mensagem': 'Turma excluída com sucesso'})
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404