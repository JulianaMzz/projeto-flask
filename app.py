from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/professores', methods=['POST'])
def criar_professor():
    dados = request.json
    if not dados or 'nome' not in dados or 'idade' not in dados or 'materia' not in dados:
        return jsonify({"error": "Nome, idade e matéria são obrigatórios"}), 400

    novo_professor = {
        "id": len(professores) + 1,
        "nome": dados["nome"],
        "idade": dados["idade"],
        "materia": dados["materia"],
        "observacoes": dados.get("observacoes", "")
    }
    professores.append(novo_professor)
    return jsonify(novo_professor), 201


@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(professores)


@app.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    professor = next((p for p in professores if p['id'] == id), None)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404
    return jsonify(professor)


@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    professor = next((p for p in professores if p['id'] == id), None)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404

    dados = request.json
    professor.update(dados)
    return jsonify(professor)


@app.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    global professores
    professores = [p for p in professores if p['id'] != id]
    return jsonify({"message": "Professor removido com sucesso"}), 200



@app.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    if not dados or 'descricao' not in dados or 'professor_id' not in dados:
        return jsonify({"error": "Descrição e professor_id são obrigatórios"}), 400

    professor = next((p for p in professores if p['id'] == dados['professor_id']), None)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404

    nova_turma = {
        "id": len(turmas) + 1,
        "descricao": dados["descricao"],
        "professor_id": dados["professor_id"],
        "ativo": dados.get("ativo", True)
    }
    turmas.append(nova_turma)
    return jsonify(nova_turma), 201


@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(turmas)


@app.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    turma = next((t for t in turmas if t['id'] == id), None)
    if not turma:
        return jsonify({"error": "Turma não encontrada"}), 404
    return jsonify(turma)

@app.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    turma = next((t for t in turmas if t['id'] == id), None)
    if not turma:
        return jsonify({"error": "Turma não encontrada"}), 404

    dados = request.json
    turma.update(dados)
    return jsonify(turma)


@app.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    global turmas
    turmas = [t for t in turmas if t['id'] != id]
    return jsonify({"message": "Turma removida com sucesso"}), 200



@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.json
    if not dados or 'nome' not in dados or 'idade' not in dados or 'turma_id' not in dados:
        return jsonify({"error": "Nome, idade e turma_id são obrigatórios"}), 400

    turma = next((t for t in turmas if t['id'] == dados['turma_id']), None)
    if not turma:
        return jsonify({"error": "Turma não encontrada"}), 404

    novo_aluno = {
        "id": len(alunos) + 1,
        "nome": dados["nome"],
        "idade": dados["idade"],
        "turma_id": dados["turma_id"],
        "data_nascimento": dados.get("data_nascimento", ""),
        "nota_primeiro_semestre": dados.get("nota_primeiro_semestre", 0.0),
        "nota_segundo_semestre": dados.get("nota_segundo_semestre", 0.0),
        "media_final": (dados.get("nota_primeiro_semestre", 0.0) + dados.get("nota_segundo_semestre", 0.0)) / 2
    }
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201


@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)


@app.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404
    return jsonify(aluno)


@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404

    dados = request.json
    aluno.update(dados)
    return jsonify(aluno)

@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    global alunos
    alunos = [a for a in alunos if a['id'] != id]
    return jsonify({"message": "Aluno removido com sucesso"}), 200

@app.route('/reset', methods=['POST'])
def resetar_dados():
    global professores, turmas, alunos
    professores = []
    turmas = []
    alunos = []
    return jsonify({"message": "Dados resetados com sucesso"}), 200




if __name__ == '_main_':
    app.run(debug=True)