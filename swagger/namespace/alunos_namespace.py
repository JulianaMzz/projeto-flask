from flask_restx import Namespace, Resource, fields
from flask import request
from alunos.alunos_model import (
    listar_alunos,
    aluno_por_id,
    adicionar_aluno,
    atualizar_aluno,
    excluir_aluno
)

alunos_ns = Namespace('alunos', description='Operações com alunos')

aluno_input = alunos_ns.model('AlunoInput', {
    'nome': fields.String(required=True, description='Nome do aluno'),
    'email': fields.String(required=True, description='Email do aluno')
})

aluno_output = alunos_ns.model('AlunoOutput', {
    'id': fields.Integer(readOnly=True),
    'nome': fields.String,
    'email': fields.String
})

@alunos_ns.route('/')
class AlunoList(Resource):
    @alunos_ns.marshal_list_with(aluno_output)
    def get(self):
        return listar_alunos()

    @alunos_ns.expect(aluno_input)
    def post(self):
        adicionar_aluno(request.json)
        return {'mensagem': 'Aluno adicionado com sucesso'}, 201

@alunos_ns.route('/<int:id_aluno>')
class Aluno(Resource):
    @alunos_ns.marshal_with(aluno_output)
    def get(self, id_aluno):
        try:
            return aluno_por_id(id_aluno)
        except ValueError as e:
            alunos_ns.abort(404, str(e))

    @alunos_ns.expect(aluno_input)
    def put(self, id_aluno):
        try:
            atualizar_aluno(id_aluno, request.json)
            return {'mensagem': 'Aluno atualizado com sucesso'}
        except ValueError as e:
            alunos_ns.abort(404, str(e))

    def delete(self, id_aluno):
        try:
            excluir_aluno(id_aluno)
            return {'mensagem': 'Aluno excluído com sucesso'}
        except ValueError as e:
            alunos_ns.abort(404, str(e))
