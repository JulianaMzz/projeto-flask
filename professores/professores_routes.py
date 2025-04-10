from flask import Blueprint, jsonify, request
from professores.professores_model import (
    listar_professores,
    professor_por_id,
    adicionar_professor,
    atualizar_professor,
    excluir_professor
)

professores_routes = Blueprint('professores_routes', __name__)


@professores_routes.route('/professores', methods=['GET'])
def rota_listar_professores():
    return jsonify(listar_professores())


@professores_routes.route('/professores/<int:id_professor>', methods=['GET'])
def rota_professor_por_id(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return jsonify(professor)
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404


@professores_routes.route('/professores', methods=['POST'])
def rota_adicionar_professor():
    novo_professor = request.get_json()
    if not novo_professor:
        return jsonify({'erro': 'Dados inválidos ou ausentes'}), 400
    
    try:
        adicionar_professor(novo_professor)
        return jsonify({'mensagem': 'Professor adicionado com sucesso'}), 201
    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400


@professores_routes.route('/professores/<int:id_professor>', methods=['PUT'])
def rota_atualizar_professor(id_professor):
    novos_dados = request.get_json()
    try:
        atualizar_professor(id_professor, novos_dados)
        return jsonify({'mensagem': 'Professor atualizado com sucesso'})
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404


@professores_routes.route('/professores/<int:id_professor>', methods=['DELETE'])
def rota_excluir_professor(id_professor):
    try:
        excluir_professor(id_professor)
        return jsonify({'mensagem': 'Professor excluído com sucesso'})
    except ValueError as erro:
        return jsonify({'erro': str(erro)}), 404