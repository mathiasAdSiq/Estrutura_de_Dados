
class No:
    def __init__(self,operacao):
        self.operacao = operacao
        self.proximo = None

def inserir(pilha,operacao):
    novo = No(operacao)

    if pilha is None:
        pilha = novo
        return pilha
    novo.proximo = pilha
    pilha = novo
    return pilha

def listar(pilha):
    aux = pilha
    contador = 1

    if pilha is None:
        print("pilha vazia")
        return
    while aux != None:
        print(contador,"=",aux.operacao)
        aux = aux.proximo
        contador += 1

def remover(pilha):
    if pilha == None:
        print("Pilha vazia")
        return

    return pilha.proximo

   
def mostrar_ultima(pilha): 
    if pilha is None: 
        print("Pilha vazia") 

        return 
    print("Última operação inserida:", pilha.operacao)        


def menu():
    print("1 - Inserir operação na pilha: ")
    print("2 - Retirar última operação (POP)")
    print("3 - Mostrar última operação inserida (topo)")
    print("4 - Mostrar todas as operações pendentes")
    print("5 - Sair")

    opc = int(input("Digite uma opção: "))
    return opc

def main():
    opc = 0
    pilha = None

    while opc != 5:
        opc = menu()
        if opc == 1:
            operacao = input("Inserir operação na pilha: ")
            pilha = inserir(pilha, operacao)

        if opc == 2:
            pilha = remover(pilha)

        if opc == 3:
            mostrar_ultima(pilha)

        if opc == 4:
            listar(pilha)

        if opc == 5:
            print("Saindo...") 
main()
