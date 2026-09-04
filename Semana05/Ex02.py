import time # Adicionado para o time.sleep funcionar

class No:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None

def adicionar(lista, parada):
    novo = No(parada)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    ultimo = lista.anterior 
    novo.proximo = lista
    novo.anterior = ultimo 
    ultimo.proximo = novo
    lista.anterior = novo
    return lista

def remover(lista, parada):
    if lista is None:
        print("A rota está vazia.")
        return None

    aux = lista
    while True:
        if aux.parada == parada:
            if aux.proximo == aux:
                print(f"Parada '{parada}' removida. A rota agora está vazia.")
                return None
            
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo

            if aux == lista:
                lista = aux.proximo

            print(f"Parada '{parada}' removida com sucesso!")
            return lista

        aux = aux.proximo 

        if aux == lista:
            print("Parada não encontrada na rota.")
            return lista

def mostrar(lista):
    if lista is None:
        print("A rota está vazia.")
        return 

    aux = lista
    print("\n// Rota Circular atual: //")
    while True:
        print(f" 🚏 chegada -> {aux.parada}")
        aux = aux.proximo 
        if aux == lista:
            break
    print()

def simular_percurso(lista, qtd_paradas):
    if lista is None:
        print("A rota está vazia. Adicione paradas primeiro.")
        return
        
    print("\n🚍 // Iniciando o trajeto do ônibus //")
    atual = lista
    
    for i in range(qtd_paradas):
        print(f"[{i+1}] O ônibus chegou na parada: {atual.parada}")
        time.sleep(0.8) 
        
        atual = atual.proximo

    print("🏁 // Fim do percurso simulado //\n")

def menu():
    print("1 - Adicionar nova parada")
    print("2 - Remover parada")
    print("3 - Mostrar rota completa")
    print("4 - Simular percurso do ônibus")
    print("5 - Sair")
    opc = int(input("Digite a opção: "))
    return opc

def main():
    rota = None
    while True:
        opc = menu()

        if opc == 1:
            nome_parada = input("Digite o nome ou número da parada: ")
            rota = adicionar(rota, nome_parada)
            print("Parada adicionada!\n")

        elif opc == 2:
            nome_parada = input("Digite o nome da parada a ser removida: ")
            rota = remover(rota, nome_parada)
            print()

        elif opc == 3:
            
            mostrar(rota)

        elif opc == 4:
            quantidade = int(input("Quantas paradas o ônibus deve percorrer na simulação? "))
            simular_percurso(rota, quantidade)

        elif opc == 5:
            print("Encerrando o sistema...")
            break 
            
        else:
            print("Opção inválida. Tente novamente.\n")


    main()
