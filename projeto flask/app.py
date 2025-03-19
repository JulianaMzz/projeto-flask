from flask import Flask, request, jsonify


app = Flask(__name__)

professores = []
turmas = []
alunos = []



@app.route('/professores', methods=['POST'])

def criar_professor():
      dados = request.json
      novo_professor = {"id": len(professores) + 1, "nome": dados["nome"]}
      professores.append(novo_professor)
      return jsonify(novo_professor), 201

@app.route('/professores', methods=['GET'])

def listar_professores():
      return jsonify(professores)



@app.route('/turmas', methods=['POST'])
def criar_turmas():
    dados = request.get_json()
    
    if not dados or 'sala' not in dados or 'professor_id' not in dados:
        return jsonify({"error": "Sala e professor_id são obrigatórios"}), 400

    nova_turma = {"id": len(turmas) + 1, "sala": dados["sala"], "professor_id": dados["professor_id"]}
    turmas.append(nova_turma)
    return jsonify(nova_turma), 201

@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(turmas)

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    data = request.get_json()
    aluno = {'id': len(alunos) + 1, 'nome': data['nome'], 'idade': data['idade'], 'turma_id': data['turma_id']}
    alunos.append(aluno)
    return jsonify(aluno), 201

@app.route('/alunos', methods=['GET'])

def listar_alunos():
      return jsonify(alunos)


if __name__ == '__main__':
      app.run(debug=True)