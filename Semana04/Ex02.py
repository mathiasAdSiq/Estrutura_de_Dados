
class No:
    def __init__(self, codigo, nome, idade, prioridade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.anterior = None
        self.proximo = None


def menu():
    print("========== MENU ==========")
    print("1 - Cadastrar paciente")
    print("2 - Remover paciente após atendimento")
    print("3 - Localizar paciente pelo código")
    print("4 - Atender paciente mais urgente")
    print("5 - Listar do primeiro para o último")
    print("6 - Listar por prioridade")
    print("7 - Listar do último para o primeiro")
    print("8 - Informar quantidade de pacientes")
    print("9 - Sair")

    return int(input("Digite sua opção: "))


def mostrar_paciente(paciente):
    print("-------------------------")
    print("Código:", paciente.codigo)
    print("Nome:", paciente.nome)
    print("Idade:", paciente.idade)
    print("Prioridade:", paciente.prioridade)


def cadastrar(lista, codigo, nome, idade, prioridade):
    novo = No(codigo, nome, idade, prioridade)

    if lista is None:
        return novo

    aux = lista

    while aux.proximo is not None:
        aux = aux.proximo

    aux.proximo = novo
    novo.anterior = aux

    return lista

def buscar(lista, codigo):
    aux = lista

    while aux is not None:
        if aux.codigo == codigo:
            return aux

        aux = aux.proximo

    return None

def remover(lista, codigo):
    paciente = buscar(lista, codigo)

    if paciente is None:
        print("Paciente não encontrado.")
        return lista


    if paciente.anterior is None:
        lista = paciente.proximo

    else:
        paciente.anterior.proximo = paciente.proximo

    if paciente.proximo is not None:
        paciente.proximo.anterior = paciente.anterior

    print("Paciente removido com sucesso!")

    return lista

def atender_mais_urgente(lista):
    if lista is None:
        print("Fila vazia.")
        return lista

    for prioridade in range(1, 6):

        aux = lista

        while aux is not None:

            if aux.prioridade == prioridade:
                print("\nPaciente atendido:")
                mostrar_paciente(aux)

                return remover(lista, aux.codigo)

            aux = aux.proximo

    return lista



def listar_primeiro_ultimo(lista):
    if lista is None:
        print("Fila vazia.")
        return

    aux = lista

    while aux is not None:
        mostrar_paciente(aux)
        aux = aux.proximo


def listar_por_prioridade(lista, prioridade):
    if lista is None:
        print("Fila vazia.")
        return

    aux = lista
    encontrou = False

    while aux is not None:

        if aux.prioridade == prioridade:
            mostrar_paciente(aux)
            encontrou = True

        aux = aux.proximo

    if encontrou is False:
        print("Não existem pacientes nessa prioridade.")


def listar_ultimo_primeiro(lista):
    if lista is None:
        print("Fila vazia.")
        return

    aux = lista

    while aux.proximo is not None:
        aux = aux.proximo

    while aux is not None:
        mostrar_paciente(aux)
        aux = aux.anterior


def quantidade(lista):
    contador = 0
    aux = lista

    while aux is not None:
        contador += 1
        aux = aux.proximo

    return contador


def main():
    lista = None
    opcao = 0

    while opcao != 9:

        opcao = menu()

        if opcao == 1:

            codigo = int(input("Digite o código: "))
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))

            print("\n1 - Emergência")
            print("2 - Muito urgente")
            print("3 - Urgente")
            print("4 - Pouco urgente")
            print("5 - Não urgente")

            prioridade = int(input("Digite a prioridade: "))

            if prioridade < 1 or prioridade > 5:
                print("Prioridade inválida.")
            else:
                lista = cadastrar(lista,codigo,nome,idade,prioridade)

                print("Paciente cadastrado com sucesso!")

        elif opcao == 2:

            codigo = int(input("Digite o código do paciente: "))
            lista = remover(lista, codigo)

        elif opcao == 3:

            codigo = int(input("Digite o código do paciente: "))
            paciente = buscar(lista, codigo)

            if paciente is not None:
                mostrar_paciente(paciente)
            else:
                print("Paciente não encontrado.")

        elif opcao == 4:

            lista = atender_mais_urgente(lista)

        elif opcao == 5:

            listar_primeiro_ultimo(lista)

        elif opcao == 6:

            prioridade = int(input("Digite a prioridade desejada: "))

            if prioridade < 1 or prioridade > 5:
                print("Prioridade inválida.")
            else:
                listar_por_prioridade(lista, prioridade)

        elif opcao == 7:

            listar_ultimo_primeiro(lista)

        elif opcao == 8:

            print("Quantidade de pacientes:", quantidade(lista))

        elif opcao == 9:

            print("Programa encerrado, Até mais.")

        else:

            print("Opção inválida!")


main()
