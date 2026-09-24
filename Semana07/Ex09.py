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

def menu():
    print("MENU:")
    print("1 - Empilhar.")
    print("2 - Desempilhar.")
    print("3 - Listar.")
    print("4 - Sair.")

    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    pilha = None

    while opc != 4:
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
                print("Até mais!")
            else:
                print("Tenta denovo!")
        except ValueError:
            print("Digita certo...")

main()
