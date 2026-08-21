class No:
    def __init__(self, id, nome, nota_final):
        self.id = id
        self.nome = nome
        self.nota_final = nota_final
        self.proximo = None
        self.anterior = None


def menu():
    print("\n1 - Inserir aluno")
    print("2 - Listar todos os alunos")
    print("3 - Remover aluno")
    print("4 - Buscar")
    print("5 - Listar alunos classificados")
    print("6 - Sair")
    opcao = int(input("Digite a opção: "))
    return opcao


def inserir_aluno(lista, id, nome, nota_final):
    novo = No(id, nome, nota_final)

    if lista is None:
        return novo

   
    novo.proximo = lista
    lista.anterior = novo
    return novo          


def listar(lista):
    aux = lista
    if aux is None:
        print("Lista vazia.")
        return

    while aux is not None:
        print("ID:", aux.id)
        print("Nome:", aux.nome)
        print("Nota Final:", aux.nota_final)
        print("-" * 20)
        aux = aux.proximo


def remover(lista, id):
    aux = lista
    anterior = None

    while aux is not None:
        if aux.id == id:
            # Caso 1: remover o primeiro nó (cabeça da lista)
            if aux == lista:
                lista = lista.proximo
                if lista is not None:
                    lista.anterior = None
            else:
                # Caso 2: remover nó do meio ou do fim
                anterior.proximo = aux.proximo
                if aux.proximo is not None:
                    aux.proximo.anterior = anterior

            print(f"Aluno '{aux.nome}' (ID {aux.id}) removido com sucesso!")
            return lista

        anterior = aux
        aux = aux.proximo          

    print(f"Aluno com ID {id} não encontrado.")
    return lista                 


def buscar(lista, id):
    aux = lista
    while aux is not None:
        if aux.id == id:
            print("ID:", aux.id)
            print("Nome:", aux.nome)
            print("Nota final:", aux.nota_final)
            return
        aux = aux.proximo

    print(f"Aluno com ID {id} não encontrado.")


def listar_classificados(lista):
    if lista is None:
        print("Lista vazia.")
        return

    aux = lista
    while aux is not None:
        if aux.nota_final >= 7:
            situacao = "Aprovado"
        elif aux.nota_final >= 4:
            situacao = "Exame"
        else:
            situacao = "Reprovado"

        print("ID:", aux.id)
        print("Nome:", aux.nome)
        print("Nota_final:", aux.nota_final)
        print("Situação:", situacao)
        print("-" * 20)

        aux = aux.proximo


def main():
    opc = 0
    lista = None

    while opc != 6:               
        opc = menu()

        if opc == 1:
            id = int(input("Digite o ID do aluno: "))
            nome = input("Digite o nome do aluno: ")
            nota_final = float(input("Digite a nota final do aluno: "))
            lista = inserir_aluno(lista, id, nome, nota_final)

        elif opc == 2:
            listar(lista)

        elif opc == 3:
            id = int(input("Digite o ID do aluno a ser removido: "))
            lista = remover(lista, id)

        elif opc == 4:
            id = int(input("Digite o ID do aluno a ser buscado: "))
            buscar(lista, id)

        elif opc == 5:
            listar_classificados(lista)

        elif opc == 6:
            print("Saindo...")

        else:
            print("Opção inválida! Tente novamente.")


main()
