
import random


class No:
    def __init__(self, guerreiro):
        self.guerreiro = guerreiro
        self.proximo = None
        self.anterior = None


def criar_guerreiros(quantidade):
    if quantidade <= 0:
        return None

    cabeca = No(1)
    atual = cabeca

    for i in range(2, quantidade + 1):
        novo = No(i)

        atual.proximo = novo
        novo.anterior = atual
        atual = novo

    atual.proximo = cabeca
    cabeca.anterior = atual

    return cabeca


def jogar(quantidade):
    if quantidade <= 0:
        print("Sem guerreiros!")
        return

    atual = criar_guerreiros(quantidade)
    restantes = quantidade
    rodada = 1

    print("\nINICIO DO JOGO")

    while restantes > 1:
        passos = random.randint(1, restantes)

        for i in range(passos - 1):
            atual = atual.proximo

        eliminado = atual

        print(f"Rodada {rodada}: "
              f"Guerreiro {eliminado.guerreiro} foi eliminado!")

        eliminado.anterior.proximo = eliminado.proximo
        eliminado.proximo.anterior = eliminado.anterior

        atual = eliminado.proximo

        restantes -= 1
        rodada += 1

    print(f"\nO SOBREVIVENTE FOI O "
          f"GUERREIRO {atual.guerreiro}!")


def menu():
    print("\nOPÇÕES:")
    print("1 - Simular partida")
    print("2 - Sair do jogo")

    try:
        opcao = int(input("Digite uma opção: "))
        return opcao

    except ValueError:
        return 0


def main():
    opcao = 0

    while opcao != 2:
        opcao = menu()

        if opcao == 1:
            try:
                quantidade = int(input("Quantidade de guerreiros: "))

                jogar(quantidade)

            except ValueError:
                print("Erro, tenta de novo!")

        elif opcao == 2:
            print("Tchau!")

        else:
            print("Opção inválida, tenta de novo!")


main()
