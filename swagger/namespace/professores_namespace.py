from flask_restx import Namespace, Resource, fields
from flask import request
from professores.professores_model import (
    listar_professores,
    professor_por_id,
    adicionar_professor,
    atualizar_professor,
    excluir_professor
)

professores_ns = Namespace('professores', description='Operações com professores')

professor_input = professores_ns.model('ProfessorInput', {
    'nome': fields.String(required=True, description='Nome do professor'),
    'email': fields.String(required=True, description='Email do professor')
})

professor_output = professores_ns.model('ProfessorOutput', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String,
    'email': fields.String
})

@professores_ns.route('/')
class ProfessorList(Resource):
    @professores_ns.marshal_list_with(professor_output)
    def get(self):
        return listar_professores()

    @professores_ns.expect(professor_input)
    def post(self):
        adicionar_professor(request.json)
        return {'mensagem': 'Professor adicionado com sucesso'}, 201

@professores_ns.route('/<int:id_professor>')
class Professor(Resource):
    @professores_ns.marshal_with(professor_output)
    def get(self, id_professor):
        try:
            return professor_por_id(id_professor)
        except ValueError as e:
            professores_ns.abort(404, str(e))

    @professores_ns.expect(professor_input)
    def put(self, id_professor):
        try:
            atualizar_professor(id_professor, request.json)
            return {'mensagem': 'Professor atualizado com sucesso'}
        except ValueError as e:
            professores_ns.abort(404, str(e))

    def delete(self, id_professor):
        try:
            excluir_professor(id_professor)
            return {'mensagem': 'Professor excluído com sucesso'}
        except ValueError as e:
            professores_ns.abort(404, str(e))

