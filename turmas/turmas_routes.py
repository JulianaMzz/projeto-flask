# turmas_routes.py

from flask import Blueprint, request, jsonify
from .turmas_model import (
    listar_turmas,
    turma_por_id,
    adicionar_turma,
    atualizar_turma,
    excluir_turma
)

# Criando o blueprint para a rota de turmas
turmas_blueprint = Blueprint('turmas', __name__)

# Rota para listar todas as turmas
@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    """Rota para listar todas as turmas."""
    return jsonify(listar_turmas())

# Rota para obter uma turma pelo ID
