
class Produto:
    def __init__(self,nome,preco,quantidade_estoque):
        self.nome = nome 
        self.preco = preco 
        self.quantidade_estoque = quantidade_estoque

    def atualizar_estoque(self,quantidade_add):
        self.quantidade_estoque += quantidade_add 

    def mostrar_resultado(self):
        print(f"Quantidade atual em estoque:{self.quantidade_estoque}")

produto_qualquer = Produto("Qualquer",100 ,5)
produto_qualquer.mostrar_resultado()
produto_qualquer.atualizar_estoque(20)
produto_qualquer.mostrar_resultado()
