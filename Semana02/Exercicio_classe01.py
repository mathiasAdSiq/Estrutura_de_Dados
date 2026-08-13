
class Produto:
    def __init__ (self,nome,preco,qtd_estoque):
        self.nome = nome 
        self.preco = preco
        self.qtd_estoque = qtd_estoque

    def mostrar_produto(self):
        print("Nome do produto:", self.nome)
        print("Preço do produto:", self.preco)
        print("Quantidade do produto:", self.qtd_estoque)

    def adicionar_produto(self):
         qtd_aumentar = int(input("Quantia de items adicionados: "))
         self.qtd_estoque += qtd_aumentar

    def vender_produto(self):
        venda = int(input("Quantia de items vendidos: "))
        self.qtd_estoque - venda

        if venda > self.qtd_estoque:
            print("Venda não disponivel, devido a falta de estoque")
        else:
            print("Venda realizada com sucesso")

    def calcular_valor(self):
        valor = self.qtd_estoque * self.preco
        
banana = Produto("Banana", 5, 30)
maca = Produto("Maça", 6, 20)
abacaxi = Produto("Abacaxi", 8, 10)
