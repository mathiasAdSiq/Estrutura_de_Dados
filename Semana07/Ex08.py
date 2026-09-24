
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

def percorrer_final(lista):
    if lista is None:
        print("Lista vazia!")
        return
    
    contador = 1
    ultimo = lista.anterior
    aux = ultimo

    while True:
        print(f"{contador} - {aux.dado};")
        contador += 1
        
        aux = aux.anterior
        
        if aux == ultimo:
            break

def remover(lista, dado_excluir):
    if lista is None:
        print("Lista vazia!")
        return
    aux = lista
    while True:
        if aux.dado == dado_excluir:
            if aux.proximo == aux:
                print("Único elemento na lista.")
                return None
            elif aux == lista:
                lista.proximo.anterior = lista.anterior
                lista.anterior.proximo = lista.proximo
                lista = lista.proximo
                return lista
            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                return lista

def menu():

    print("1 - Inserir.")
    print("2 - Percorrer.")
    print("3 - Inserir no final.")
    print("4 - Percorrer ao contrário.")
    print("5 - Remover.")
    print("6 - Sair.")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    lista = None

    while opc != 6:
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
                percorrer_final(lista)
            elif opc == 5:
                dado = int(input("Digite um dado para excluir:"))
                lista = remover(lista, dado)
            elif opc == 6:
                print("Até mais!")
            else:
                print("Digite de novo!")

        except ValueError:
            print("opção invalida")

main()        
