
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


def inserir(fila_inicio, fila_fim, dado):
    novo = No(dado)

    if fila_inicio is None:
        fila_inicio = novo
        fila_fim = novo
        return fila_fim, fila_inicio

    fila_fim.proximo = novo
    novo.anterior = fila_fim
    fila_fim = novo
    return fila_inicio, fila_fim

def listar(fila_inicio):
    aux = fila_inicio
    contador = 1

    if fila_inicio == None:
        print("Lista vazia")
        return

    while aux != None:
        print(contador, "=", aux.dado)
        contador +=1 
        aux = aux.proximo

def remover(fila_inicio, fila_fim):
    if fila_inicio is None:
        print("Fila vazia")
        return None, None
    if fila_inicio == fila_fim:
        print("Unico elemento na fila")
        return None, None

    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None
    return fila_inicio, fila_fim


def menu():
    print("1 - Inserir na fila")
    print("2 - Listar fila")
    print("3 - Remover da fila")
    print("4 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc


def main():
    opcao = 0
    fila_inicio = None
    fila_fim = None

    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            dado = int(input("Digite um dado: "))
            fila_inicio, fila_fim = inserir(fila_inicio,fila_fim,dado)
        elif opcao == 2:
            listar(fila_inicio)
        elif opcao == 3:
            fila_inicio, fila_fim = remover(fila_inicio, fila_fim)
            listar(fila_inicio)
        elif opcao == 4:
            print("Saindo....")
        
main()
