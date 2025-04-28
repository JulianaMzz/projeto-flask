from flask_restx import Namespace, Resource, fields
from flask import request
from turmas.turmas_model import (
    listar_turmas,
    turma_por_id,
    adicionar_turma,
    atualizar_turma,
    excluir_turma
)

turmas_ns = Namespace('turmas', description='Operações com turmas')

turma_input = turmas_ns.model('TurmaInput', {
    'nome': fields.String(required=True, description='Nome da turma'),
    'turno': fields.String(required=True, description='Turno da turma')
})

turma_output = turmas_ns.model('TurmaOutput', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String,
    'turno': fields.String
})

@turmas_ns.route('/')
class TurmaList(Resource):
    @turmas_ns.marshal_list_with(turma_output)
    def get(self):
        return listar_turmas()

    @turmas_ns.expect(turma_input)
    def post(self):
        adicionar_turma(request.json)
        return {'mensagem': 'Turma adicionada com sucesso'}, 201

@turmas_ns.route('/<int:id_turma>')
class Turma(Resource):
    @turmas_ns.marshal_with(turma_output)
    def get(self, id_turma):
        try:
            return turma_por_id(id_turma)
        except ValueError as e:
            turmas_ns.abort(404, str(e))

    @turmas_ns.expect(turma_input)
    def put(self, id_turma):
        try:
            atualizar_turma(id_turma, request.json)
            return {'mensagem': 'Turma atualizada com sucesso'}
        except ValueError as e:
            turmas_ns.abort(404, str(e))

    def delete(self, id_turma):
        try:
            excluir_turma(id_turma)
            return {'mensagem': 'Turma excluída com sucesso'}
        except ValueError as e:
            turmas_ns.abort(404, str(e))
