
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):
        if self.cargo =="Gerente":
            soma =  self.salario*   0.1


        else: 
            soma = self.salario*    0.05

        self.salario = self.salario + soma
        print(self.salario)
        

Patrao = Funcionario("Pedro", 5000,"Gerente")

Peao = Funcionario ("Joao", 1800, "Atendente" )

Patrao.calcular_bonus()
Peao.calcular_bonus()
