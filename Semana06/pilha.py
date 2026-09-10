
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


def inserir(pilha, dado):
    no = No(dado)
    if pilha == None:
        pilha = no
        return pilha
    no.proximo = pilha
    pilha = no
    return pilha

def listar(pilha):
    aux = pilha
    contador = 1

    if pilha == None:
        print("Pilha vazia")
        return
    while aux != None:
        # print(contador, " = " aux.dado)
        print(f"{contador}  = {aux.dado}")
        aux = aux.proximo 
        contador = contador + 1
        # contador += 1

def remover(pilha):
    if pilha == None:
        print("Pilha vazia")
        return None

    return pilha.proximo

def menu():
    print("1 - Inserir na pilha")
    print("2 - Listar pilha")
    print("3 - Remover da pilha")
    print("4 - Sair")
    opc = int(input("Digite a opção: "))
    return opc

def main():
    opc = 0
    pilha = None

    while opc != 4:
        opc = menu()
        if opc == 1:
            dado = int(input("Digite um dado: "))
            pilha = inserir(pilha, dado)
        elif opc == 2:
            listar(pilha)
        elif opc == 3:
            pilha = remover(pilha)
            listar(pilha)
        elif opc ==4:
            print("Saindo....")



main()
