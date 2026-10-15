

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

            

def menu():

    print("1 - Adicionar cliente comum no fim da fila (chamado comum).")
    print("2- Adicionar cliente preferencial no início da fila (chamado urgente).")
    print("3 - Atender chamado (remoção do primeiro).")
    print("4 - Listar todos os chamados da fila.")
    print("5 - Sair do sistema.")
    opc = int(input("Digite a opção: "))
    return opc

def main():
    opc = 0
    deque = Deque()

    while opc != 5:
        opc = menu()
        if opc == 1:
            dado = input("Digite o nome do cliente: ")
            deque.inserir_fim(dado)

        if opc == 2:
            dado = input("Digite o nome do cliente: ")
            deque.inserir_inicio(dado)

        if opc == 3:
            deque.excluir_inicio(dado)

        if opc == 4: 
            deque.mostrar_lista()

        if opc == 5:
            print("Saindo.....")    

main()
