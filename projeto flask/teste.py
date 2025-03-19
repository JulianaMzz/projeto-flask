import requests


res = requests.post("http://127.0.0.1:5000/professores", json={"nome": "Manoel da Silva"})
if res.status_code == 201:
    try:
        print("Criar professor:", res.json())
    except ValueError:
        print("Resposta não contém JSON válido", res.text)
else:
    print(f"Erro {res.status_code}: {res.text}")


res = requests.post("http://127.0.0.1:5000/turmas", json={"sala": "102", "professor_id": 1})
if res.status_code == 201:
    print("Criar Turma:", res.json())
else:
    print(f"Erro {res.status_code}: {res.text}")


res = requests.post("http://127.0.0.1:5000/alunos", json={"nome": "Manoel da Silva", "idade": 17, "turma_id": 1})
if res.status_code == 201:
    print("Criar Aluno:", res.json())
else:
    print(f"Erro {res.status_code}: {res.text}")


res = requests.get("http://127.0.0.1:5000/alunos")
if res.status_code == 200:
    print("Listar Alunos:", res.json())
else:
    print(f"Erro {res.status_code}: {res.text}")
