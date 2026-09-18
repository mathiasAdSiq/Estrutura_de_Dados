
class No:

    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

class NoDuplo:
    def __init__(self):
        self.inicio = None
        self.fim = None


def adicionar_inicio(lista, nome):
    novo = No(nome)

    if lista is None:
        lista = novo
        return lista
    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista

def percorrer_frente(lista):

    if lista is None:
        print("Lista vazia")
        return
    aux = lista
    contador = 1

    while aux is not None:

        print(contador, "-", aux.nome)
        contador += 1
        aux = aux.proximo

def percorrer_tras(lista):

    if lista is None:
        print("Lista vazia")
        return
    aux = lista
    

    while aux.proximo is not None:
        aux = aux.proximo
        contador = 1

    while aux is not None:

        print(contador, "-", aux.nome)
        contador += 1
        aux = aux.anterior


def menu():

    print("1 - Adicionar jogador")
    print("2 - Percorrer do primeiro ao ultimo")
    print("3 - Percorrer do ultimo ao primeiro")
    print("4 - Sair")

    opc = int(input("Digite a opção: "))
    return opc


def main():

    opc = 0
    lista = None

    while opc != 4:
        opc = menu()

        if opc == 1:
            nome = input("Digite o nome do jogador: ")
            lista = adicionar_inicio(lista, nome)

        elif opc == 2:
            percorrer_frente(lista)
        elif opc == 3:
            percorrer_tras(lista) 
        elif opc == 4:
            print("Saindo...")

        else:
            print("Opção inválida")


main()
