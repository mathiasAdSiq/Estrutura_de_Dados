
class Aluno:
    def __init__(self,nome,notas):
        self.nome = nome
        self.notas = notas
        self.media = 0 

    def calcular_media(self):
        soma = 0

        for i in range(len(self.notas)):
            soma += self.notas[i]
            self.media = soma/ len(self.notas)
        return self.media

    def verificar_aprovacao(self):
        
        if  self.media  >= 7:
            print("Aprovado") 

        else:
            print("Reprovado")


nota1 = [4,5,8]
nota2 = [9,7,7]

aluno1 = Aluno("Alan", nota1)
aluno1.calcular_media()
aluno1.verificar_aprovacao()
print(aluno1.nome, aluno1.calcular_media())

aluno2 = Aluno("Pedro", nota2)
aluno2.calcular_media()
aluno2.verificar_aprovacao()
print(aluno2.nome, aluno2.calcular_media())
