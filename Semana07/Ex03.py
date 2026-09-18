

class No:

    def __init__(self, nome,gols):
        self.nome = nome
        self.proximo = None
        self.gols = gols


def adicionar_nome(lista, nome,gols):
    novo = No(nome,gols)

    if lista is None:
        lista = novo
        return lista
    novo.proximo = lista
    lista = novo
    return lista

def adicionar_final(lista, nome,gols):
    novo = No(nome,gols)

    if lista is None:
        lista = novo
        return lista

    aux = lista
    
    while aux.proximo != None:
        aux = aux.proximo
    aux.proximo = novo
    return lista

def percorrer(lista):

    if lista is None:
        print("lista vazia")
        return
    aux = lista
    contador = 1

    while aux is not None:
        print(contador,"-",aux.nome)
        contador +=1
        aux = aux.proximo

def calcular_media(lista):

    if lista is None:
        print("Lista vazia")
        return
    aux = lista
    contador = 0
    soma = 0 

    while aux is not None:
        soma += aux.gols
        contador +=1
        aux = aux.proximo

    media = soma/contador
    print("Média de gols:",media)



def mostrar(lista):

    if lista is None:
        print("Lista vazia")
        return
    aux = lista
    contador = 1

    while aux is not None:

        print(contador, "-", aux.nome, aux.gols, "Gols")
        contador += 1
        aux = aux.proximo

def menu():

    print("1 - Adicionar jogador")
    print("2 - Mostrar jogadores")
    print("3 - Adicionar no final")
    print("4 - Percorrer a lista")
    print("5 - calcular media")
    print("6 - Sair")

    opc = int(input("Digite a opção: "))
    return opc


def main():

    opc = 0
    lista = None

    while opc != 6:
        opc = menu()

        if opc == 1:
            nome = input("Digite o nome do jogador: ")
            gols = int(input("Digite o número de gols realidazo pelo jogador: "))
            lista = adicionar_nome(lista, nome, gols)

        elif opc == 2:
            mostrar(lista)
        elif opc == 3:
            nome = input("Digite o nome do jogador: ")
            gols = int(input("Digite o número de gols realidazo pelo jogador: "))
            adicionar_final(lista,nome, gols)

        elif opc == 4:
            percorrer(lista)

        elif opc == 5:
            calcular_media(lista)

        elif opc == 6:
            print("Saindo...")

        else:
            print("Opção inválida")


main()
