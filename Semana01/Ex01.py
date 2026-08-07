
class Produto: 
    def __init__(self, nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total():
        total = self.preco * self.quantidade
        return total

    def mostrar_produto(self):
        print("Nome do produto:", self.nome)
        print("Preço do produto:", self.preco)
        print("Quantidade do produto:", self.quantidade)
        print("Total do produto:", self.calcular_total())

produto1 = Produto("Notebook", 3000, 2)
produto1.mostrar_produto()

