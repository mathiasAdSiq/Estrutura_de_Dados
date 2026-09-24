class NoDuploCircular:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


def adicionar_inicio(lista, dado):
    novo = NoDuploCircular(dado)

    
    if lista is None:
        lista = novo
        novo.proximo = novo
        novo.anterior = novo
        return lista

    
    novo.proximo = lista
    novo.anterior = lista.anterior
    lista.anterior.proximo = novo
    lista.anterior = novo

    lista = novo

    return lista


def percorrer(lista):
    if lista is None:
        print("Lista vazia")
        return

    contador = 1
    aux = lista

    while True:
        print(contador, "-", aux.dado)
        contador += 1

        aux = aux.proximo

        if aux == lista:
            break


def menu():
    print("1 - Inserir")
    print("2 - Percorrer")
    print("3 - Sair")

    opc = int(input("Digite uma opção: "))
    return opc


def main():
    lista = None
    opc = 0

    while opc != 3:
        try:
            opc = menu()

            if opc == 1:
                dado = int(input("Digite um dado: "))
                lista = adicionar_inicio(lista, dado)

            elif opc == 2:
                percorrer(lista)

            elif opc == 3:
                print("Saindo...")
                

            else:
                print("Opção inválida!")

        except ValueError:
            print("Tente novamente!")


main()
