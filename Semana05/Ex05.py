
class No:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None


def inserir(lista, nome, idade, prioridade):
    novo = No(nome, idade, prioridade)

    if lista is None:
        novo.proximo = novo
        return novo

    aux = lista

    while aux.proximo != lista:
        aux = aux.proximo

    aux.proximo = novo
    novo.proximo = lista

    return lista

def remover(lista, nome):
    if lista is None:
        print("Sem pacientes.")
        return None

    aux = lista
    anterior = None

    if lista.proximo == lista:
        if lista.nome == nome:
            print(f"Paciente {nome} removido.")
            return None

        print("Paciente não encontrado.")
        return lista

    while True:
        if aux.nome == nome:

            if aux == lista:
                ultimo = lista

                while ultimo.proximo != lista:
                    ultimo = ultimo.proximo

                lista = lista.proximo
                ultimo.proximo = lista

            else:
                anterior.proximo = aux.proximo

            print(f"Paciente {nome} removido.")
            return lista

        anterior = aux
        aux = aux.proximo

        if aux == lista:
            break

    print("Paciente não encontrado.")
    return lista

def mostrar(lista):
    if lista is None:
        print("Sem pacientes.")
        return

    aux = lista

    while True:
        print(f"Nome: {aux.nome}, "
              f"Idade: {aux.idade}, "
              f"Prioridade: {aux.prioridade}")

        aux = aux.proximo

        if aux == lista:
            break

def simular(lista):
    if lista is None:
        print("Sem pacientes.")
        return None

    ordem_prioridades = ["EMERGÊNCIA","URGÊNCIA","NORMAL"]

    for prio in ordem_prioridades:

        while True:
            if lista is None:
                break
            encontrou = False
            aux = lista
            while True:

                if aux.prioridade == prio:
                    print(f"Atendendo: "
                          f"{aux.nome} ({aux.prioridade})")

                    lista = remover(lista, aux.nome)

                    encontrou = True
                    break

                aux = aux.proximo

                if aux == lista:
                    break

            if not encontrou:
                break
    print("Todos os atendimentos foram concluídos.")
    return None
def menu():
    print("\nMENU:")
    print("1 - Inserir paciente na fila.")
    print("2 - Remover paciente atendido.")
    print("3 - Mostrar todos os pacientes na ordem.")
    print("4 - Simular atendimento.")
    print("5 - Sair.")

    opc = int(input("Digite uma opção: "))

    return opc

def main():
    opc = 0
    lista = None

    while opc != 5:
        opc = menu()

        if opc == 1:
            try:
                nome = input( "Digite o nome do paciente: ").title()

                idade = int(input("Digite a idade do paciente: "))

                while idade < 0 or idade > 100:
                    idade = int(input("Digite novamente: "))

                prioridade = input("Digite a prioridade do paciente""(EMERGÊNCIA, URGÊNCIA, NORMAL): ").upper()

                while prioridade not in ("EMERGÊNCIA","URGÊNCIA","NORMAL"):
                    prioridade = input("Digite novamente: ").upper()

                lista = inserir(lista,nome,idade,prioridade)

            except ValueError:
                print("Erro, tenta denovo!")

        elif opc == 2:
            try:
                nome = input("Digite o nome do paciente: ").title()

                lista = remover(lista, nome)

            except ValueError:
                print("Erro, tenta denovo!")

        elif opc == 3:
            mostrar(lista)

        elif opc == 4:
            lista = simular(lista)

        elif opc == 5:
            print("Até mais!")

        else:
            print("Erro, tenta denovo!")

main()
