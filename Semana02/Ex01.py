

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None 

def menu():
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Retirar item")
    print("4 - Sair")
    opcao = int(input("Digite a opcao:"))
    return opcao

def inserir(lista, dado):
    no = No(dado)

    
    if lista == None:
        lista = no 
        return lista

    no.proximo = lista
    lista = no
    return lista

def listar(lista):
    aux = lista 
    while aux != None:

        print(" - ", aux.dado)
        aux = aux.proximo



def remover(lista, dado):
    aux = lista 
    anterior = None

    if lista == None:
        print("Lista vazia")
        return 

    while aux != None:
        if aux.dado == dado:
            if aux == lista: # Primeiro elemento da lista
                lista = lista.proximo
                return lista
            else:
                anterior.proximo = aux.proximo
                return lista
        anterior = aux    
        aux = aux.proximo

    print("Dado não encontrado")
    return lista

def main():
    lista = None  
    opcao = 0

    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            dado = int(input("Digite um dado:"))
            lista = inserir(lista, dado)
        elif opcao == 2:
            listar(lista)
        
        elif opcao == 3:
            dado = int(input("Dado para retirar:"))
            lista = remover(lista, dado)

main()
