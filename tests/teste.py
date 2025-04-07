import unittest
import requests

URL = "http://127.0.0.1:5000"

class TesteAPI(unittest.TestCase):

    def setUp(self):
        """Método executado antes de cada teste. Reseta os dados e cria os dados básicos."""
        self.resetar_dados()

        
        self.professor_dados = {
            "nome": "Camily",
            "idade": 22,
            "materia": "Química",
            "observacoes": "Muito querida pelos alunos"
        }
        self.turma_dados = {
            "descricao": "6º ano B",
            "professor_id": None,  
            "ativo": True
        }
        self.aluno_dados = {
            "nome": "Carlos",
            "idade": 13,
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 7.5
        }

    def tearDown(self):
        """Método executado após cada teste. Caso necessário, limpar recursos ou realizar ações de cleanup."""
        pass 

    def resetar_dados(self):
        """Método para resetar os dados do banco."""
        resposta = requests.post(f"{URL}/reset")
        self.assertEqual(resposta.status_code, 200, f"Erro ao resetar os dados: {resposta.text}")

    def teste_professor(self):
        """Testa a criação, consulta, atualização e deleção de um professor."""
        resposta = requests.post(f"{URL}/professores", json=self.professor_dados)
        self.assertEqual(resposta.status_code, 201, f"Erro ao criar professor: {resposta.text}")
        professor = resposta.json()
        self.assertIn('id', professor)
        self.assertIn('nome', professor)
        self.assertIn('idade', professor)

        id_prof = professor["id"]

       
        resposta = requests.get(f"{URL}/professores/{id_prof}")
        self.assertEqual(resposta.status_code, 200, f"Erro ao obter professor: {resposta.text}")

        resposta = requests.put(f"{URL}/professores/{id_prof}", json={"idade": 35})
        self.assertEqual(resposta.status_code, 200, f"Erro ao atualizar professor: {resposta.text}")
        self.assertEqual(resposta.json()["idade"], 35)

        resposta = requests.delete(f"{URL}/professores/{id_prof}")
        self.assertEqual(resposta.status_code, 200, f"Erro ao deletar professor: {resposta.text}")

    def teste_turma(self):
        """Testa a criação, consulta, atualização e deleção de uma turma."""
      
        professor = requests.post(f"{URL}/professores", json={"nome": "Lucas", "idade": 40, "materia": "História"}).json()

        self.turma_dados["professor_id"] = professor["id"]

        resposta = requests.post(f"{URL}/turmas", json=self.turma_dados)
        self.assertEqual(resposta.status_code, 201, f"Erro ao criar turma: {resposta.text}")
        turma = resposta.json()
        id_turma = turma["id"]

    
        resposta = requests.get(f"{URL}/turmas/{id_turma}")
        self.assertEqual(resposta.status_code, 200, f"Erro ao obter turma: {resposta.text}")

        resposta = requests.put(f"{URL}/turmas/{id_turma}", json={"descricao": "6º ano B - Atualizado"})
        self.assertEqual(resposta.status_code, 200, f"Erro ao atualizar turma: {resposta.text}")
        self.assertEqual(resposta.json()["descricao"], "6º ano B - Atualizado")

      
        resposta = requests.delete(f"{URL}/turmas/{id_turma}")
        self.assertEqual(resposta.status_code, 200, f"Erro ao deletar turma: {resposta.text}")

    def teste_aluno(self):
        """Testa a criação, consulta, atualização e deleção de um aluno."""

        professor = requests.post(f"{URL}/professores", json={"nome": "Juliana", "idade": 29, "materia": "Geografia"}).json()

        turma = requests.post(f"{URL}/turmas", json={"descricao": "7º ano A", "professor_id": professor["id"]}).json()

        self.aluno_dados["turma_id"] = turma["id"]

        resposta = requests.post(f"{URL}/alunos", json=self.aluno_dados)
        self.assertEqual(resposta.status_code, 201, f"Erro ao criar aluno: {resposta.text}")
        aluno = resposta.json()
        self.assertIn('id', aluno)
        self.assertIn('nome', aluno)
        self.assertIn('idade', aluno)

        id_aluno = aluno["id"]

        resposta = requests.get(f"{URL}/alunos/{id_aluno}")
        self.assertEqual(resposta.status_code, 200, f"Erro ao obter aluno: {resposta.text}")

       
        resposta = requests.put(f"{URL}/alunos/{id_aluno}", json={"idade": 14})
        self.assertEqual(resposta.status_code, 200, f"Erro ao atualizar aluno: {resposta.text}")
        self.assertEqual(resposta.json()["idade"], 14)

        resposta = requests.delete(f"{URL}/alunos/{id_aluno}")
        self.assertEqual(resposta.status_code, 200, f"Erro ao deletar aluno: {resposta.text}")

if __name__ == '__main__':
    unittest.main()