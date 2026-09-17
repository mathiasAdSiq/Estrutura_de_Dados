
class No:
    def __init__(self, jogador):
        self.jogador = jogador
        self.proximo = None

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, jogador):

        novo = No(jogador)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo

        else:
            self.fim.proximo = novo
            self.fim = novo

    def remover(self):

        if self.inicio is None:
            return None

        jogador = self.inicio.jogador

        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        return jogador

    def rodada(self):

        if self.inicio is None:
            print("Fila vazia.")
            return

        jogador = self.remover()

        print(f"Jogador da rodada: {jogador}")


        self.adicionar(jogador)


    def varias_rodadas(self, n):

        if self.inicio is None:
            print("Fila vazia.")
            return

        for i in range(1, n + 1):

            print(f"--- Rodada {i} ---")

            jogador = self.remover()

            print(f"{jogador} jogou!")

            self.adicionar(jogador)

            print("Fila:", end=" ")

            self.mostrar()

    def mostrar(self):

        if self.inicio is None:
            print("Fila vazia.")
            return

        atual = self.inicio

        while atual is not None:

            print(atual.jogador, end="")

            if atual.proximo is not None:
                print(" -> ", end="")

            atual = atual.proximo

        print()

    def proximo_jogador(self):

        if self.inicio is None:
            print("Fila vazia.")
            return

        print(f"Próximo a jogar: {self.inicio.jogador}")

    def limpar(self):

        self.inicio = None
        self.fim = None

        print("Fila limpa.")

def menu():

    print("===== SALA DE PARTIDAS =====")
    print("1 - Adicionar jogador ao final da fila")
    print("2 - Simular 1 rodada")
    print("3 - Simular N rodadas")
    print("4 - Mostrar fila")
    print("5 - Mostrar próximo a jogar")
    print("6 - Limpar fila")
    print("7 - Sair")

    opcao = int(input("Digite uma opção: "))

    return opcao

def main():

    fila = Fila()

    opcao = 0

    while opcao != 7:

        opcao = menu()

        if opcao == 1:
            jogador = input("Digite o nome do jogador: ")
            fila.adicionar(jogador)
            print(f"{jogador} entrou na fila.")

        elif opcao == 2:
            fila.rodada()

        elif opcao == 3:
            n = int(input("Quantas rodadas deseja simular? "))
            fila.varias_rodadas(n)

        elif opcao == 4:
            print("\nFila:")
            fila.mostrar()

        elif opcao == 5:
            fila.proximo_jogador()

        elif opcao == 6:
            fila.limpar()

        elif opcao == 7:
            print("Programa encerrado.")

        else:
            print("Opção inválida.")

main()
