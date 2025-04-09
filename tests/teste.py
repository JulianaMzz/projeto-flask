import unittest
import requests

URL = "http://127.0.0.1:5000"

class TesteAPI(unittest.TestCase):

    def setUp(self):
        self.resetar_dados()
        self.professor_dados = {
            "id": 1,
            "nome": "Camily",
            "idade": 22,
            "disciplina": "Química"
        }
        self.turma_dados = {
            "id": 1,
            "nome": "6º ano B",
            "turno": "Manhã"
        }
        self.aluno_dados = {
            "id": 1,
            "nome": "Carlos",
            "idade": 13,
            "turma_id": 1,
            "data_nascimento": "2010-01-01",
            "nota_1_semestre": 8.5,
            "nota_2_semestre": 7.5,
            "media_final": 8.0
        }

    def resetar_dados(self):
        resposta = requests.post(f"{URL}/reset")
        self.assertEqual(resposta.status_code, 200)

    def teste_professor(self):
        resposta = requests.post(f"{URL}/professores", json=self.professor_dados)
        self.assertEqual(resposta.status_code, 201)

        resposta = requests.get(f"{URL}/professores/1")
        self.assertEqual(resposta.status_code, 200)
        dados = resposta.json()
        self.assertEqual(dados["nome"], "Camily")

        resposta = requests.put(f"{URL}/professores/1", json={"idade": 30})
        self.assertEqual(resposta.status_code, 200)

        resposta = requests.delete(f"{URL}/professores/1")
        self.assertEqual(resposta.status_code, 200)

    def teste_turma(self):
        requests.post(f"{URL}/turmas", json=self.turma_dados)

        resposta = requests.get(f"{URL}/turmas/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["nome"], "6º ano B")

        resposta = requests.put(f"{URL}/turmas/1", json={"turno": "Tarde"})
        self.assertEqual(resposta.status_code, 200)

        resposta = requests.delete(f"{URL}/turmas/1")
        self.assertEqual(resposta.status_code, 200)

    def teste_aluno(self):
        requests.post(f"{URL}/turmas", json=self.turma_dados)
        requests.post(f"{URL}/alunos", json=self.aluno_dados)

        resposta = requests.get(f"{URL}/alunos/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["nome"], "Carlos")

        resposta = requests.put(f"{URL}/alunos/1", json={"idade": 14})
        self.assertEqual(resposta.status_code, 200)

        resposta = requests.delete(f"{URL}/alunos/1")
        self.assertEqual(resposta.status_code, 200)

if __name__ == '__main__':
    unittest.main()