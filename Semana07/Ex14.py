class Fila:
    def __init__(self, usuarios, tempo):
        self.usuarios = usuarios
        self.tempo = tempo
        self.proximo = None
        self.anterior = None

def enfileirar(fila_inicio, fila_fim, usuario, tempo):
    novo = Fila(usuario, tempo)

    if fila_inicio is None:
        fila_inicio = novo
        fila_fim = novo
        return fila_inicio, fila_fim

    fila_fim.proximo = novo
    novo.anterior = fila_fim
    fila_fim = novo
    return fila_inicio, fila_fim

def desenfileirar(fila_inicio, fila_fim):
    if fila_inicio is None:
        print("Lista vazia!")
        return None, None

    if fila_inicio == fila_fim:
        print("Único elemento na lista!")
        return None, None

    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None
    return fila_inicio, fila_fim

def percorrer(fila_inicio):
    if fila_inicio is None:
        print("Fila vazia!")
        return

    aux = fila_inicio
    while aux is not None:
        print(f"- {aux.usuarios};")
        aux = aux.proximo

def proximo(fila_inicio):
    if fila_inicio is None:
        print("Fila vazia!")
        return

    aux = fila_inicio
    while aux is not None:
        print(f"Próximo a ser atendido: {aux.usuarios};")
        break

def esta_vazia(fila_inicio):
    if fila_inicio is None:
        print("A fila está vazia!")
        return    
    else:
        print("A fila não está vazia!")
        return

def tamanho(fila_inicio):
    if fila_inicio is None:
        print("Fila vazia!")
        return

    contador = 0
    aux = fila_inicio
    while aux is not None:
        contador += 1
        aux = aux.proximo
    print(f"Quantidade de pessoas na fila:{contador}")

def tempo_atendimento(fila_inicio):
    if fila_inicio is None:
        print("Fila vazia!")
        return 

    contador = 0
    soma_tempo = 0
    aux = fila_inicio
    while aux != None:
        soma_tempo += aux.tempo
        contador += 1
        aux = aux.proximo
    media = soma_tempo / contador
    print(f"Média da espera dos atendimentos dos usuários: {media}.")

def menu():
    print("\nMENU:")
    print("1 - Enfileirar.")
    print("2 - Desenfileirar.")
    print("3 - Percorrer.")
    print("4 - Próximo a ser atendido.")
    print("5 - Fila vazia ou não.")
    print("6 - Tamanho da fila.")
    print("7 - Tempo de atendimento da fila.")
    print("8 - Sair.")

    opc = int(input("Digite uma opção:"))
    return opc

def main():
    opc = 0
    fila_inicio = None
    fila_fim = None

    while opc != 8:
        try:
            opc = menu()
            if opc == 1:
                usuario = input("Digite seu nome:").title()
                tempo = float(input("Digite o seu tempo de espera máximo:"))
                fila_inicio, fila_fim = enfileirar(fila_inicio, fila_fim, usuario, tempo)
            elif opc == 2:
                fila_inicio, fila_fim = desenfileirar(fila_inicio, fila_fim)
            elif opc == 3:
                percorrer(fila_inicio)
            elif opc == 4:
                proximo(fila_inicio)
            elif opc == 5:
                esta_vazia(fila_inicio)
            elif opc == 6:
                tamanho(fila_inicio)
            elif opc == 7:
                tempo_atendimento(fila_inicio)
            elif opc == 8:
                print("Até mais!")
            else:
                print("Tenta denovo!")

        except ValueError:
            print("Digita certo...")

main()
