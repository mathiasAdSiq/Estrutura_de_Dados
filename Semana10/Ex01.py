
class No:
    def __init__(self,dado):
         self.dado = dado
         self.proximo = None
         self.anterior = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_inicio(self, dado):
        novo = No(dado)

        if self.head is None:
             self.head = self.tail = novo
             return

        novo.proximo = self.head
        self.head.anterior = novo
        self.head = novo

    def inserir_fim(self, dado):
        novo = No(dado)

        if self.tail is None:
            self.tail = self.head = novo
            return
        novo.anterior = self.tail
        self.tail.proximo = novo
        self.tail = novo        


    def mostrar_lista(self):
        if self.head == None:
            print("Deque vazio")
            return
        aux = self.head
        while aux!= None:
            print("-",aux.dado)
            aux = aux.proximo   


    def excluir_inicio(self, dado):
        if self.head == None:
            print("Deque vazio")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.proximo
        self.head.anterior = None

            
    def excluir_fim(self, dado):
        if self.tail is None:
            print("Deque vazio")
            return

        elif self.tail == self.head:
            self.tail = self.head = None
            return
        
        self.tail = self.tail.anterior
        self.tail.proximo = None


def menu():

    print("1 - Adicionar chamado no fim da fila (chamado comum).")
    print("2- Adicionar chamado no início da fila (chamado urgente).")
    print("3 - Atender chamado do início da fila (remoção do primeiro).")
    print("4 - Atender chamado do fim da fila (remoção do último).")
    print("5 - Listar todos os chamados da fila.")
    print("6 - Sair do sistema.")
    opc = int(input("Digite a opção: "))
    return opc

def main():
    opc = 0
    deque = Deque()

    while opc != 6:
        opc = menu()
        if opc == 1:
            dado = int(input("Digite o dado: "))
            deque.inserir_fim(dado)

        if opc == 2:
            dado = int(input("Digite o dado: "))
            deque.inserir_inicio(dado)

        if opc == 3:
            deque.excluir_inicio(dado)

        if opc == 4:
            deque.excluir_fim(dado)

        if opc == 5: 
            deque.mostrar_lista()

        if opc == 6:
            print("Saindo.....")    

main()
