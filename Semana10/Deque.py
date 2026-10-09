
class No:
    def __init__(self,dado):
         self.dado = dado
         self.proximo = None
         self.anterior = None

class Deque:
    def __init__(self):
        self.head = None # Cabeça da lista
        self.tail = None # Cauda da lista

    # Inserir na cabeça
    def inserir_cabeca(self, dado):
        novo = No(dado)

        if self.head is None:
             self.head = self.tail = novo
             return
        novo.proximo = self.head 
        self.head.anterior = novo
        self.head = novo

    def inserir_cauda(self, dado):
        novo = No(dado)

        if self.tail is None:
            self.tail = self.head = novo
            return
        novo.anterior = self.tail
        self.tail.proximo = novo
        self.tail = novo


    def mostrar_cabeca(self):
        if self.head == None:
            print("Deque vazio")
            return
        aux = self.head
        while aux!= None:
            print("-",aux.dado)
            aux = aux.proximo
    
    def mostrar_cauda(self):
        if self.tail == None:
            print("Deque vazio")
            return
        aux = self.tail
        while aux != None:
            print("-", aux.dado)
            aux = aux.anterior

    def excluir_cabeca(self, dado):
        if self.head == None:
            print("Deque vazio")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.proximo
        self.head.anterior = None

            
    def excluir_cauda(self, dado):
        if self.tail is None:
            print("Deque vazio")
            return

        elif self.tail == self.head:
            self.tail = self.head = None
            return
        
        self.tail = self.tail.anterior
        self.tail.proximo = None

def menu():
    print("1 - Inserir na cabeça")
    print("2 - Inserir na cauda")
    print("3 - Excluir item na cabeça")
    print("4 - Excluir item na calda")
    print("5 - Mostrar deque pela cabeça")
    print("6 - Mostrar deque pela cauda")
    print("7 - Sair")
    opc = int(input("Opcão: "))
    return opc


def main():
    opc = 0
    deque = Deque()

    while opc != 7:
        opc = menu()
        if opc == 1:
            
            dado = int(input("Digite o dado: "))
            deque.inserir_cabeca(dado)
            print("Dado na cabeça: ",deque.head.dado)

        elif opc == 2:
            dado = int(input("Digite o dado: "))
            deque.inserir_cauda(dado)
            print("Dado na cauda: ",deque.tail.dado)

        elif opc == 3:
            deque.excluir_cabeca(dado)
        elif opc == 4:
            deque.excluir_cauda(dado)
        elif opc == 5:
             deque.mostrar_cabeca()
        elif opc == 6:
            deque.mostrar_cauda()
        elif opc == 7:
            print("Saindo...")

main()

        
