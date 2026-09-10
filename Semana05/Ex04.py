import random

class No:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None
        self.anterior = None

def mesa(cliente):
    if cliente <= 0:
        return None

    novo = No(1)
    aux = novo

    for i in range(2, cliente + 1):
        novo_no = No(i)

        aux.proximo = novo_no
        novo_no.anterior = aux

        aux = novo_no

    aux.proximo = novo
    novo.anterior = aux

    return novo


def adicionar_cliente(novo, id_cliente):
    novo_no = No(id_cliente)

    if novo is None:
        novo_no.proximo = novo_no
        novo_no.anterior = novo_no

        return novo_no

    ultimo = novo.anterior

    ultimo.proximo = novo_no
    novo_no.anterior = ultimo
    novo_no.proximo = novo
    novo.anterior = novo_no

    return novo

def remover_cliente(novo, no_remover):
    if novo is None or no_remover is None:
        return None, None

    if novo.proximo == novo and novo == no_remover:
        return None, None

    proximo_no = no_remover.proximo

    no_remover.anterior.proximo = no_remover.proximo
    no_remover.proximo.anterior = no_remover.anterior

    novo = proximo_no if novo == no_remover else novo

    return novo, proximo_no

def simular(cliente):
    if cliente <= 0:
        print("Sem clientes!")
        return

    novo = mesa(cliente)
    aux = novo
    total_restante = cliente
    proximo_id = cliente + 1

    print("\nComeçando o rodízio.")

    while total_restante > 1:
        passos = random.randint(1, 5)

        print("A fatia de pizza está passando...")

        for _ in range(passos):
            aux = aux.proximo
            print(f"Cliente {aux.cliente} recebeu a fatia.")

        acao = random.choice(["nada", "adicionar", "remover"])

        if acao == "adicionar":
            novo = adicionar_cliente(novo, proximo_id)

            total_restante += 1

            print(f"Cliente {proximo_id} entrou na mesa!")

            proximo_id += 1

        elif acao == "remover" and total_restante > 1:
            cliente_removido = aux.cliente

            novo, aux = remover_cliente(novo, aux)

            total_restante -= 1

            print(f"Cliente {cliente_removido} se mandou!")

    print(f"\nRodízio encerrado! Apenas o cliente {aux.cliente} sobrou.")

def menu():
    print("\nOPÇÕES:")
    print("1 - Simular rodízio.")
    print("2 - Sair.")

    try:
        opc = int(input("Escolha uma opção: "))

        return opc

    except ValueError:
        print("Erro ao digitar.")

        return -1

def main():
    opc = 0

    while opc != 2:
        opc = menu()

        if opc == 1:
            try:
                cliente = int(input("Digite a quantidade de clientes: "))

                simular(cliente)

            except ValueError:
                print("Erro, tenta denovo!")

        elif opc == 2:
            print("Até mais!!")

        else:
            print("Erro, tenta denovo!")


main()
