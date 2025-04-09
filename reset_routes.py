from flask import Blueprint, jsonify
from alunos.alunos_model import dados as dados_alunos
from professores.professores_model import dados as dados_professores
from turmas.turmas_model import dados as dados_turmas

reset_routes = Blueprint("reset_routes", __name__)

@reset_routes.route('/reset', methods=['POST'])
def reset():
    dados_alunos["alunos"].clear()
    dados_professores["professores"].clear()
    dados_turmas["turmas"].clear()

    return jsonify({"mensagem": "Dados resetados com sucesso"}), 200