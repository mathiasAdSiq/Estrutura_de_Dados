
class NoDuploCircular:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

def adicionar(lista, dado):
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

def adiciona_final(lista, dado):
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
    
    return lista

def percorrer(lista):
    if lista is None:
        print("Lista vazia!")
        return
    
    contador = 1
    aux = lista
    while aux is not None:
        print(f"{contador} - {aux.dado};")
        contador += 1
        if aux.proximo == lista:
            return
        aux = aux.proximo

def menu():

    print("1 - Inserir.")
    print("2 - Percorrer.")
    print("3 - Inserir no final.")
    print("4 - Sair.")

    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    lista = None

    while opc != 4:
        try:
            opc = menu()
            if opc == 1:
                dado = int(input("Digite um dado:"))
                lista = adicionar(lista, dado)
            elif opc == 2:
                percorrer(lista)
            elif opc == 3:
                dado = int(input("Digite um dado:"))
                lista = adiciona_final(lista, dado)
            elif opc == 4:
                print("Até mais!")
            else:
                print("Digite de novo!")

        except ValueError:
            print("opção invalida")

main()        
