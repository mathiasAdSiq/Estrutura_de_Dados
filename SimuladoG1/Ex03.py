class Circular:
    def __init__(self, nome, duracao, ambiente, ativo):
        self.nome = nome
        self.duracao = duracao
        self.ambiente = ambiente
        self.ativo = ativo
        self.proximo = None


def adicionar(lista, nome, duracao, ambiente, ativo):
    novo = Circular(nome, duracao, ambiente, ativo)

    if lista is None:
        novo.proximo = novo
        return novo

    aux = lista

    while aux.proximo != lista:
        aux = aux.proximo

    aux.proximo = novo
    novo.proximo = lista

    return lista


def listar(lista):
    if lista is None:
        print("Lista vazia!")
        return

    ambientes = ["teste", "homologação", "produção"]

    for ambiente in ambientes:
        aux = lista

        while True:
            if aux.ambiente == ambiente:
                print(aux.nome + ", " + str(aux.duracao) + " segundos, " +
                      aux.ambiente + ", ativo: " + str(aux.ativo))

            aux = aux.proximo

            if aux == lista:
                break


def listar_ativos(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista
    encontrou = False

    while True:
        if aux.ativo:
            print(aux.nome + ", " + str(aux.duracao) + " segundos, " +
                  aux.ambiente)
            encontrou = True

        aux = aux.proximo

        if aux == lista:
            break

    if not encontrou:
        print("Não há deploys ativos.")


def exibir(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista
    total_tempo = 0

    while True:
        total_tempo += aux.duracao
        aux = aux.proximo

        if aux == lista:
            break

    print("Tempo total:", total_tempo, "segundos")


def alterar_status(lista, nome, status):
    if lista is None:
        print("Lista vazia!")
        return lista

    aux = lista

    while True:
        if aux.nome == nome:
            aux.ativo = status

            if status:
                print("Deploy ativado.")
            else:
                print("Deploy desativado.")

            return lista

        aux = aux.proximo

        if aux == lista:
            break

    print("Deploy não encontrado.")
    return lista


def remover(lista, nome):
    if lista is None:
        print("Lista vazia!")
        return lista

    aux = lista
    anterior = lista

    while anterior.proximo != lista:
        anterior = anterior.proximo

    while True:
        if aux.nome == nome:
            if aux.proximo == aux:
                return None

            anterior.proximo = aux.proximo

            if aux == lista:
                lista = aux.proximo

            print("Deploy removido.")
            return lista

        anterior = aux
        aux = aux.proximo

        if aux == lista:
            break

    print("Deploy não encontrado.")
    return lista


def menu():
    print("\nMENU:")
    print("1 - Adicionar deploy")
    print("2 - Listar todos os deploys")
    print("3 - Exibir o tempo total")
    print("4 - Ativar um deploy")
    print("5 - Desativar um deploy")
    print("6 - Excluir um deploy")
    print("7 - Sair")

    return int(input("Digite uma opção: "))


def main():
    lista = None
    opcao = 0

    while opcao != 7:
        try:
            opcao = menu()

            if opcao == 1:
                nome = input("Digite o nome do deploy: ")
                duracao = int(input("Digite a duração em segundos: "))
                ambiente = input(
                    "Digite o ambiente (teste, homologação ou produção): "
                ).lower()

                if ambiente not in ["teste", "homologação", "produção"]:
                    print("Ambiente inválido.")
                elif duracao < 0:
                    print("A duração não pode ser negativa.")
                else:
                    lista = adicionar(lista, nome, duracao, ambiente, True)

            elif opcao == 2:
                print("1 - Listar por ambiente")
                print("2 - Listar apenas os deploys ativos")

                escolha = int(input("Digite uma opção: "))

                if escolha == 1:
                    listar(lista)
                elif escolha == 2:
                    listar_ativos(lista)
                else:
                    print("Opção inválida.")

            elif opcao == 3:
                exibir(lista)

            elif opcao == 4:
                nome = input("Digite o nome do deploy para ativar: ")
                lista = alterar_status(lista, nome, True)

            elif opcao == 5:
                nome = input("Digite o nome do deploy para desativar: ")
                lista = alterar_status(lista, nome, False)

            elif opcao == 6:
                nome = input("Digite o nome do deploy para excluir: ")
                lista = remover(lista, nome)

            elif opcao == 7:
                print("Saindo....")

            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite um valor válido.")


main()
