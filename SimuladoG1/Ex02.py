class No:
    def __init__(self, id, nome, status=False):
        self.id = id
        self.nome = nome
        self.status = status
        self.proximo = None
        self.anterior = None


def inserir(lista, id, nome, status=False):
    novo = No(id, nome, status)

    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo

    return lista


def remover(lista, id):
    if lista is None:
        print("Lista vazia!")
        return lista

    aux = lista

    while aux is not None:
        if aux.id == id:
            if aux.anterior is None:
                lista = aux.proximo

                if lista is not None:
                    lista.anterior = None
            else:
                aux.anterior.proximo = aux.proximo

                if aux.proximo is not None:
                    aux.proximo.anterior = aux.anterior

            return lista

        aux = aux.proximo

    print(id, "não encontrado!")
    return lista


def ligar_desligar(lista, id):
    
    aux = lista

    while aux is not None:
        if aux.id == id:
            aux.status = not aux.status
            return lista

        aux = aux.proximo

    print(id, "não encontrado!")
    return lista


def percorrer_normal(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista

    while aux is not None:
        print("-", aux.id, aux.nome, aux.status)
        aux = aux.proximo


def percorrer_contrario(lista):
    if lista is None:
        print("Lista vazia!")
        return

    aux = lista

    while aux.proximo is not None:
        aux = aux.proximo

    while aux is not None:
        print("-", aux.id, aux.nome, aux.status)
        aux = aux.anterior


def main():
    lista = None

    lista = inserir(lista, 9874, "Pedro", True)
    lista = inserir(lista, 7149, "Puntel", True)
    lista = inserir(lista, 8243, "Vini", False)

    print()
    percorrer_normal(lista)

    print()
    percorrer_contrario(lista)

    lista = remover(lista, 9874)

    print()
    percorrer_normal(lista)


main()
