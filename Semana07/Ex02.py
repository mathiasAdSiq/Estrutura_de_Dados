
class No:

    def __init__(self, nome):
        self.nome = nome
        self.proximo = None


def adicionar_nome(lista, nome):
    novo = No(nome)

    if lista is None:
        lista = novo
        return lista
    novo.proximo = lista
    lista = novo
    return lista

def adicionar_final(lista, nome):
    novo = No(nome)

    if lista is None:
        return novo
    aux = lista
    anterior = None

    while aux != None:
        anterior = aux
        aux = aux.proximo
    anterior.proximo = novo
    return lista


def mostrar(lista):

    if lista is None:
        print("Lista vazia")
        return
    aux = lista
    contador = 1

    while aux is not None:

        print(contador, "-", aux.nome)
        contador += 1
        aux = aux.proximo

def menu():

    print("1 - Adicionar jogador")
    print("2 - Mostrar jogadores")
    print("3 - Adicionar no final")
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
            lista = adicionar_nome(lista, nome)

        elif opc == 2:
            mostrar(lista)
        elif opc == 3:
            nome = input("Digite o nome do jogador: ")
            adicionar_final(lista,nome)
        elif opc == 4:
            print("Saindo...")

        else:
            print("Opção inválida")


main()
