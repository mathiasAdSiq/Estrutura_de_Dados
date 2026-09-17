
class No:

    def __init__(self, carro):
        self.carro = carro
        self.proximo = None


def inserir(pilha, carro):

    novo = No(carro)

    if pilha is None:
        pilha = novo
        return pilha

    novo.proximo = pilha
    pilha = novo

    return pilha


def listar(pilha):

    aux = pilha
    contador = 1

    if pilha is None:
        print("Pilha vazia")
        return

    while aux is not None:

        print(f"{contador} = {aux.carro}")

        aux = aux.proximo
        contador = contador + 1


def remover_ate_carro(pilha, carro_desejado):

    if pilha is None:
        print("Pilha vazia")
        return pilha

    encontrou = False

    print("Carros retirados:")

    while pilha is not None:


        if pilha.carro == carro_desejado:
            print(pilha.carro)
            encontrou = True

            pilha = pilha.proximo

            break

        print(pilha.carro)

        pilha = pilha.proximo

    if not encontrou:
        print("Carro não encontrado.")

    return pilha


def menu():

    print("===== GARAGEM =====")
    print("1 - Mostrar todos os carros")
    print("2 - Remover um carro específico")
    print("3 - Sair")

    opc = int(input("Digite uma opção: "))

    return opc


def main():

    opcao = 0
    pilha = None

    carros = [
        "Fusca","Onix","Tracker","Montana","Equinox","Argo","Cronos","Mobi",
        "Fastback","Strada","Corolla","Corolla Cross","Hilux","Uno",
        "Escort","Corcel","Del Rey","Maverick","Gol","Civic"
    ]


    for carro in carros:
        pilha = inserir(pilha, carro)


    while opcao != 3:

        opcao = menu()

        if opcao == 1:
            listar(pilha)

        elif opcao == 2:
            carro_desejado = input("Digite o carro para ser removido: ")
            pilha = remover_ate_carro(pilha,carro_desejado)

        elif opcao == 3:
            print("Saindo...")

        else:
            print("Opção inválida")

main()
