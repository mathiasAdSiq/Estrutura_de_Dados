
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

aluno1 = Aluno("Alan", [5, 8, 9])
aluno2 = Aluno("Pedro", [6, 7, 8])
aluno3 = Aluno("João", [9, 7, 10])

turma = [aluno1, aluno2, aluno3]

for aluno in turma:
    print("Nome:", aluno.nome)
    print("Média:", aluno.calcular_media())
    print()
