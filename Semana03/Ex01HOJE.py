
class No:
    def __init__(self, id , nome, nota_final):
        self.id = id
        self.nome = nome
        self.nota_final = nota_final
        self.proximo = None 
        self.anterior = None



def menu():
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Buscar")
    print("5 - Listar alunos classificados")
    print("6 - Sair")
    opcao = int(input("Digite a opção: "))
    return opcao

def inserir_aluno(lista, id, nome, nota_final):
    novo = No(id, nome, nota_final)
    if lista is None:
        lista = novo
        return lista 




def listar(self, lista):
    aux = lista
    while aux != None:
        print("ID:", aux.id)
        print("Nome:", aux.nome)
        print("Nota Final:", aux.nota_final)
        print()
        aux = aux.proximo

def remover(lista, id):
    aux = lista
    anterior = None 
    while aux != None:
        if aux.id == id:
            if aux == lista:
                lista = lista.proximo
                if lista is not None:
                    lista .anterior = None
                    return lista
                else:
                    anterior.proximo = aux.proximo
                    if aux.proximo is not None:
                        aux.proximo.anterior = anterior
                        return lista


def buscar(lista, id):
    aux = lista
    while aux != None:
        if aux.id == id:
            print("ID:", aux.id)
            print("Nome:", aux.nome)
            print("Nota final :", aux.nota_final)
            return
        aux = aux.proximo

def listar_classificador(lista):
    aux = lista
    while aux != None:
        if aux.nota_final >=6:
            print("ID:", aux.id)
            print("Nome:", aux.nome)
            print("Nota_final:", aux.nota_final)
            print()


def main():
    opc = 0 
    lista = None
    while opc != 4:
        opc = menu()

        if opc == 1:
            id = int(input("Digite o ID do aluno: "))
            nome = input("Digite o nome do aluno: ")
            nota_final = float(input("digite a nota final do aluno: "))
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



main()
