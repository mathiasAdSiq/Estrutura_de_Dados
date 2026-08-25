class No:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.atual = None
        self.total = 0

    def inserir(self, id, nome, artista, duracao):
        novo = No(id, nome, artista, duracao)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            self.atual = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.total += 1

    def listar(self):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        print("\nLista de músicas:")

        aux = self.inicio

        while aux is not None:
            print(f"ID: {aux.id}")
            print(f"Nome: {aux.nome}")
            print(f"Artista: {aux.artista}")
            print(f"Duração: {aux.duracao} minutos")

            if aux == self.atual:
                print(">>> Música atual <<<")


            aux = aux.proximo

    def remover(self, id):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        aux = self.inicio

        while aux is not None and aux.id != id:
            aux = aux.proximo

        if aux is None:
            print(f"Música com ID {id} não encontrada.")
            return


        if aux == self.inicio and aux == self.fim:
            self.inicio = None
            self.fim = None
            self.atual = None

        elif aux == self.inicio:
            self.inicio = aux.proximo
            self.inicio.anterior = None

            if self.atual == aux:
                self.atual = self.inicio

        elif aux == self.fim:
            self.fim = aux.anterior
            self.fim.proximo = None

            if self.atual == aux:
                self.atual = self.fim


        else:
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if self.atual == aux:
                self.atual = aux.proximo

        self.total -= 1

        print(f"Música com ID {id} removida com sucesso!")

    def verificacao_nome(self, nome):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        aux = self.inicio
        encontrado = False

        while aux is not None:
            if aux.nome.upper() == nome.upper():
                print(f"Encontramos a música: {aux.nome}")
                print(f"Artista: {aux.artista}")
                print(f"Duração: {aux.duracao} minutos")
                encontrado = True

            aux = aux.proximo

        if not encontrado:
            print(f"Música {nome} não encontrada.")

    def verificacao_artista(self, artista):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        aux = self.inicio
        encontrado = False

        while aux is not None:
            if aux.artista.upper() == artista.upper():
                print(f"Música: {aux.nome}")
                print(f"Artista: {aux.artista}")
                print(f"Duração: {aux.duracao} minutos")
                
                encontrado = True

            aux = aux.proximo

        if not encontrado:
            print(f"Artista {artista} não encontrado.")

    def verificacao_id(self, identificador):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        aux = self.inicio
        encontrado = False

        while aux is not None:
            if aux.id == identificador:
                print(f"Encontramos o ID {aux.id} na playlist.")
                print(f"Música: {aux.nome}")
                print(f"Artista: {aux.artista}")
                print(f"Duração: {aux.duracao} minutos")
                encontrado = True

            aux = aux.proximo

        if not encontrado:
            print(f"Não encontramos o ID {identificador} na playlist.")

    def duracao_total(self):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        aux = self.inicio
        total = 0

        while aux is not None:
            total += aux.duracao
            aux = aux.proximo

        print(f"Duração total da playlist: {total:.2f} minutos.")

    def proxima_musica(self):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        if self.atual.proximo is None:
            print("Você já está na última música.")
            return

        self.atual = self.atual.proximo

        print(f"Agora tocando: {self.atual.nome}")
        print(f"Artista: {self.atual.artista}")

    def musica_anterior(self):
        if self.inicio is None:
            print("Playlist vazia.")
            return

        if self.atual.anterior is None:
            print("Você já está na primeira música.")
            return

        self.atual = self.atual.anterior

        print(f"Agora tocando: {self.atual.nome}")
        print(f"Artista: {self.atual.artista}")


def menu():
   
    print("1 - Adicionar música")
    print("2 - Listar músicas")
    print("3 - Remover música")
    print("4 - Buscar música")
    print("5 - Mostrar duração total")
    print("6 - Avançar para próxima música")
    print("7 - Voltar para música anterior")
    print("8 - Sair")


    opc = int(input("Digite a sua opção: "))

    return opc


def main():
    lista = ListaDuplamenteEncadeada()

    opc = 0

    while opc != 8:

        opc = menu()

        if opc == 1:
            nome = input("Digite o nome da música: ").upper()
            artista = input("Digite o artista: ").upper()
            identificador = int(input("Digite o ID da música: "))
            duracao = float(input("Digite a duração em minutos: "))

            lista.inserir(
                identificador,
                nome,
                artista,
                duracao
            )

            print("Música adicionada com sucesso!")

        elif opc == 2:
            lista.listar()

        elif opc == 3:
            identificador = int(input("Digite o ID da música para remover: "))

            lista.remover(identificador)

        elif opc == 4:
            n_or_id = int(input("Deseja buscar pelo nome(1), artista(2) ou ID(3)? "))

            if n_or_id == 1:
                nome = input("Digite o nome da música para a busca: ")

                lista.verificacao_nome(nome)

            elif n_or_id == 2:
                artista = input("Digite o nome do artista para a busca: ")

                lista.verificacao_artista(artista)

            elif n_or_id == 3:
                identificador = int(input("Digite o ID da música para a busca: "))
                lista.verificacao_id(identificador)

            else:
                print("Tente novamente com uma opção válida!")

        elif opc == 5:
            lista.duracao_total()

        elif opc == 6:
            lista.proxima_musica()

        elif opc == 7:
            lista.musica_anterior()

        elif opc == 8:
            print("Tchau!")

        else:
            print("Digite outra opção, esta é inválida!")


main()
