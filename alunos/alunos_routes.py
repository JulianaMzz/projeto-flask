from flask import Blueprint, request, jsonify
from .alunos_model import (
    listar_alunos,
    aluno_por_id,
    adicionar_aluno,
    atualizar_aluno,
    excluir_aluno
)

alunos_blueprint = Blueprint('alunos', __name__)
