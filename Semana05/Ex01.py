

class Time:
    def __init__(self,id,bastao=False):
        self.id = id
        self.bastao = bastao
        self.proximo = None
        self.anterior = None

def adicionar(lista,id,bastao):
        novo = Time(id,bastao)

        if lista is None:
            novo.proximo = novo
            novo.anterior = novo
            lista = novo
            return novo

        novo.proximo = lista
        novo.anterior = lista.anterior
        lista.proximo.anterior = novo
        lista.anterior.proximo = novo
        lista = novo 
        return lista

def remover(lista,id):
    aux = lista

    if lista is None:
            print("lista vazia")
            return 

    
    aux = lista
    while True:
        if aux.id == id:
            if aux.proximo == aux:
                print(f"Atleta{id} removido. a lista está vazia agora.")
                return None
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo

            if aux == lista:
                lista = aux.proximo
            print(f"Atleta {id} removido.")
            return lista             

        elif aux == lista: 

            print("Atleta não encontrado.")
            return lista

def simular(lista, turnos):

    if lista is None:
        print("lista vazia")
        return
    aux = lista
    atleta_com_bastao = None

    while True:
        if aux.bastao:
              atleta_com_bastao = aux
              break
        aux = aux.proximo
        if aux == lista:
              break

    if atleta_com_bastao is None:
        print("Ninguem tinha o bastao. Entregando ao primeiro atleta.")
        lista.bastao = True 
        atleta_com_bastao = lista 

        print("// Iniciando a simulação //")
        atual = atleta_com_bastao
        for i in range(turnos):
            print("Turno {i+1}: O atleta '{atual.id}' está com o bastão.")
            

            atual.bastao = False
            atual = atual.proximo
            atual.bastao = True 

        print("// Finalizando a Simulação //")

def mostrar(lista):
    if lista is None:
          print("lista vazia")
          return

    aux = lista
    print("Atletas na equipe: ")
    while True:
         status = "Com bastão " if aux.bastao else "Sem bastão"
         print(f" Atleta {aux.id} ({status}) ")
         aux = aux.proximo
         if aux == lista:
              break

    print()
         



def menu():
        print("1 - Inserir atleta")
        print("2 - Remover atleta")
        print("3 - simular corrida de bastão ")
        print("4 -  Mostrar time")
        print("5 - Sair")
        opc = int(input("Digite a opção: "))
        return opc


def main():
    lista = None
    while True:
        opc = menu()

        if opc == 1:
            id_atleta = input("Digite o ID(nome/número) do atleta: ")
            bastao_input = input("Ele possui o bastão agora? (s/n): ").strip().lower()  
            bastao = True if bastao_input == "s" else False
            lista = adicionar(lista, id_atleta, bastao)
            print("Atleta adicionado!")

        elif opc == 2:
            id_atleta = input("Digite o ID do atleta a ser removido: ")
            lista = remover(lista,id_atleta)

        elif opc == 3:
             turnos = int(input("Quantos passes de bastão deseja simular? "))
             simular(lista, turnos)

        elif opc == 4:
             mostrar(lista)

        elif opc == 5:
             print("Saindo....")


main()
