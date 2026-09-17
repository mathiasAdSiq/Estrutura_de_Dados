
class No:

    def __init__(self, carro):
        self.carro = carro
        self.proximo = None


def inserir(pilha, carro):

    novo = No(carro)

    if pilha is None:
        return novo

    novo.proximo = pilha

    return novo


def listar(pilha):

    if pilha is None:
        print("Pilha vazia")
        return

    aux = pilha
    contador = 1

    while aux is not None:

        print(f"{contador} - {aux.carro}")

        aux = aux.proximo
        contador += 1


def remover_ate_carro(pilha, carro_desejado):

    if pilha is None:
        print("Pilha vazia")
        return pilha

    encontrou = False

    print("\nCarros retirados:")

    while pilha is not None:

        # Mostra o carro que está saindo
        print(pilha.carro)

        # Se encontrou o carro desejado,
        # remove ele também e encerra
        if pilha.carro == carro_desejado:
            encontrou = True
            pilha = pilha.proximo
            break

        # Remove o carro do topo
        pilha = pilha.proximo

    if not encontrou:
        print("Carro não encontrado.")

    return pilha


    if not encontrou:
        print("Carro não encontrado.")

    else:
        print(f"O carro {carro_desejado} está pronto para sair.")

    return pilha


def menu():

    print("\n===== GARAGEM =====")
    print("1 - Mostrar todos os carros")
    print("2 - Remover um carro específico")
    print("3 - Sair")

    opc = int(input("Digite uma opção: "))

    return opc


def main():

    pilha = None

    # 20 carros cadastrados
    carros = [
        "Fusca",
        "Onix",
        "Tracker",
        "Montana",
        "Equinox",
        "Argo",
        "Cronos",
        "Mobi",
        "Fastback",
        "Strada",
        "Corolla",
        "Corolla Cross",
        "Hilux",
        "Uno",
        "Escort",
        "Corcel",
        "Del Rey",
        "Maverick",
        "Gol",
        "Civic"
    ]

    # Colocando os 20 carros na pilha
    for carro in carros:
        pilha = inserir(pilha, carro)

    opcao = 0

    while opcao != 3:

        opcao = menu()

        if opcao == 1:

            print("\nCarros na garagem:")
            listar(pilha)

        elif opcao == 2:

            carro_desejado = input(
                "Digite o nome do carro que deseja retirar: "
            )

            pilha = remover_ate_carro(
                pilha,
                carro_desejado
            )

        elif opcao == 3:

            print("Programa encerrado.")

        else:

            print("Opção inválida.")


main()
