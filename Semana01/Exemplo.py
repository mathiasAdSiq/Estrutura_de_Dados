
class Aluno:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.disciplinas = 0
        self.situacao = True

    def alterar_disciplinas(self, disciplinas):
        self.disciplinas = disciplinas 

    def mostrar_quantidade_disciplinas(self):
        print("Quantidade de disciplinas: ", self.disciplinas)
    
    def alterar_situacao(self):
        if self.situacao == True:
            self.situacao = False
        else:
            self.situacao = True
        
    def mostrar_situacao(self):
        print("Nome:", self.nome)
        print('Situação:', self.situacao)
        self.mostrar_quantidade_disciplinas()

luis = Aluno("Luis Eduardo", 18,"Recanto Maestro")
luis.mostrar_situacao()
luis.alterar_situacao()
luis.alterar_disciplinas(10)
luis.mostrar_situacao()

print()
luis = Aluno("Luiz Alawi",18,"TecnoAMF")
luis.mostrar_situacao()
