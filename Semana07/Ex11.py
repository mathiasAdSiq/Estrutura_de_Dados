class Pilha:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def empilhar(pilha, dado):
    novo = Pilha(dado)

    if pilha is None:
        pilha = novo
        return pilha

    novo.proximo = pilha
    pilha = novo
    return pilha

def desempilhar(pilha):
    if pilha is None:
        print("Lista vazia!")
        return 

    return pilha.proximo

def listar(pilha):
    if pilha is None:
        print("Lista vazia!")
        return

    contador = 1
    aux = pilha
    while aux is not None:
        print(f"{contador} - {aux.dado};")
        aux = aux.proximo

def topo(pilha):
    if pilha is None:
        print("Lista vazia!")
        return

    aux = pilha
    while aux is not None:
        print(f"Primeiro elemento: {aux.dado};")
        break

def esta_vazia(pilha):
    if pilha is None:
        print(" A pilha está vazia!")
        return
    else:
        print("A lista não está vazia")

def quantidade(pilha):
    if pilha is None:
        print("Lista vazia!")
        return   
    contador = 0
    aux = pilha
    while aux is not None:
        contador += 1
        aux = aux.proximo
    print(f"Quantidade de elementos:{contador}")

def menu():
    print("\nMENU:")
    print("1 - Empilhar.")
    print("2 - Desempilhar.")
    print("3 - Listar.")
    print("4 - Topo da pilha")
    print("5 - Verificar se a lista está vazia.")
    print("6 - Quantidade de elementos.")
    print("7 - Sair.")

    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    pilha = None

    while opc != 7:
        try:
            opc = menu()
            if opc == 1:
                dado = int(input("Digite um dado:"))
                pilha = empilhar(pilha, dado)
            elif opc == 2:
                pilha = desempilhar(pilha)
            elif opc == 3:
                listar(pilha)
            elif opc == 4:
                topo(pilha)
            elif opc == 5:
                esta_vazia(pilha)
            elif opc == 6:
                quantidade(pilha)
            elif opc == 7:
                print("Até mais!")
            else:
                print("Tenta denovo!")
        except ValueError:
            print("Digita certo...")

main()
