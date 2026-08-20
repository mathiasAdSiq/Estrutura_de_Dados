
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def menu():
    print("1 - inserir item.")
    print("2 - listar itens.")
    print("3 - Retirar Itens.")
    print("4 - Alterar sinal da Lista.")
    print("5 - Sair.")
    opcao = int(input("Digite a opção:"))
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
        print("Lista vazia.")
        return lista
 
    while aux != None:
        if aux.dado == dado:
            if aux == lista:
                lista = lista.proximo
                return lista
            else:
                anterior.proximo = aux.proximo
                return lista
        anterior = aux
        aux = aux.proximo
    print("Dado não encontrado.")
    return lista

def lista_insere_final(lista, valor):
    no = No(valor)
    if lista == None:
        return no
    aux = lista
    anteriro = None
    while aux != None:
        anterior = aux
        aux = aux.proximo
    anterior.proximo = no
    return lista

def lista_calcula_media(lista):
    if lista == None:
        print("Lista vazia")
        return
    aux = lista
    soma = 0
    contador = 0
    while aux != None:
        soma += aux.dado
        contador += 1
        aux = aux.proximo
    media = soma / contador
    print(f"Média dos dados da lista: {media}")


def lista_altera(lista):
    if lista == None:
        print("Lista vazia")
        return 
    aux = lista
    while aux != None:
        
        aux.dado = -aux.dado
        aux = aux.proximo

def main():
    lista = None
    opc = 0
    
    while opc != 5:
        opc = menu()
        if opc == 1:
            dado = float(input("Digite um dado:"))
            lista = inserir(lista,dado)
        elif opc == 2:
            listar(lista)
        elif opc == 3:
            dado = float(input("Dado parar retirar:"))
            lista = remover(lista, dado)
        elif opc == 4:
            lista_altera(lista)
main()
