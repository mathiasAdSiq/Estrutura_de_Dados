

class No:
    def __init__(self, matricula, nome, nota_final):
        self.matricula = matricula
        self.nome = nome
        self.situacao = True
        self.nota_final = nota_final
        self.proximo = None

def menu():
    print("========== MENU ==========")
    print("1 - Cadastrar um aluno no final da lista")
    print("2 - Listar todos os alunos cadastrados")
    print("3 - Listar apenas alunos ativos")
    print("4 - Listar apenas alunos desativados")
    print("5 - Buscar um aluno pela matrícula")
    print("6 - Alterar nota final de um aluno")
    print("7 - Alterar a situação do aluno")
    print("8 - Remover um aluno da lista")
    print("9 - Informar a quantidade de alunos cadastrados")
    print("10 - Calcular a média das notas da turma")
    print("11 - Calcular a média das notas dos alunos ativos")
    print("12 - Sair")

    opcao = int(input("Digite a sua opção: "))

    return opcao

def cadastrar_final(lista, matricula, nome, nota_final):
    novo = No(matricula, nome, nota_final)

    if lista is None:
        return novo

    aux = lista

    while aux.proximo is not None:
        aux = aux.proximo
   
    aux.proximo = novo

    return lista


def listar_alunos_cadastrados(lista):
    if lista is None:
        print("Lista vazia.")
        return

    aux = lista

    while aux is not None:
        print("-------------------------")
        print("Matrícula:", aux.matricula)
        print("Nome:", aux.nome)
        print("Situação:", aux.situacao)
        print("Nota final:", aux.nota_final)

        aux = aux.proximo


def listar_alunos_ativos(lista):
    if lista is None:
        print("Lista vazia.")
        return

    aux = lista
    encontrou = False

    while aux is not None:

        if aux.situacao == True:
            print("-------------------------")
            print("Matrícula:", aux.matricula)
            print("Nome:", aux.nome)
            print("Situação:", aux.situacao)
            print("Nota final:", aux.nota_final)

            encontrou = True

        aux = aux.proximo

    if encontrou == False:
        print("Não existem alunos ativos.")



def listar_alunos_desativados(lista):
    if lista is None:
        print("Lista vazia.")
        return

    aux = lista
    encontrou = False

    while aux is not None:

        if aux.situacao == False:
            print("-------------------------")
            print("Matrícula:", aux.matricula)
            print("Nome:", aux.nome)
            print("Situação:", aux.situacao)
            print("Nota final:", aux.nota_final)

            encontrou = True

        aux = aux.proximo

    if encontrou == False:
        print("Não existem alunos desativados.")


def buscar(lista, matricula):
    aux = lista

    while aux is not None:

        if aux.matricula == matricula:
            return aux

        aux = aux.proximo

    return None

def alterar_nota(lista, matricula, nova_nota):
    aluno = buscar(lista, matricula)

    if aluno is None:
        print("Aluno não encontrado.")
        return

    aluno.nota_final = nova_nota

    print("Nota alterada com sucesso!")

def alterar_situacao(lista, matricula):
    aluno = buscar(lista, matricula)

    if aluno is None:
        print("Aluno não encontrado.")
        return

    aluno.situacao = not aluno.situacao

    print("Situação alterada com sucesso!")
    print("Nova situação:", aluno.situacao)

def remover(lista, matricula):

    if lista is None:
        print("Lista vazia.")
        return lista

    if lista.matricula == matricula:
        lista = lista.proximo
        print("Aluno removido com sucesso!")
        return lista

    
    aux = lista

    while aux.proximo is not None:

        if aux.proximo.matricula == matricula:
            aux.proximo = aux.proximo.proximo

            print("Aluno removido com sucesso!")
            return lista

        aux = aux.proximo

    print("Aluno não encontrado.")

    return lista


def quantidade_alunos(lista):
    quantidade = 0
    aux = lista

    while aux is not None:
        quantidade += 1
        aux = aux.proximo

    return quantidade

def media_turma(lista):

    if lista is None:
        return 0

    soma = 0
    quantidade = 0

    aux = lista

    while aux is not None:
        soma += aux.nota_final
        quantidade += 1

        aux = aux.proximo

    return soma / quantidade


def media_ativos(lista):

    soma = 0
    quantidade = 0

    aux = lista

    while aux is not None:

        if aux.situacao == True:
            soma += aux.nota_final
            quantidade += 1

        aux = aux.proximo

    if quantidade == 0:
        return 0

    return soma / quantidade


def main():

    lista = None

    opcao = 0

    while opcao != 12:

        opcao = menu()

        if opcao == 1:

            matricula = int(input("Digite o número da matrícula: "))

            nome = input("Digite o nome do aluno: ")

            nota_final = float(input("Digite a nota final: "))

            lista = cadastrar_final(lista,matricula,nome,nota_final)

            print("Aluno cadastrado com sucesso!")

        elif opcao == 2:
            listar_alunos_cadastrados(lista)

        elif opcao == 3:
            listar_alunos_ativos(lista)

        elif opcao == 4:
            listar_alunos_desativados(lista)

        elif opcao == 5:

            matricula = int(input("Digite a matrícula do aluno: "))
            aluno = buscar(lista, matricula)

            if aluno is not None:
                print("-------------------------")
                print("Aluno encontrado!")
                print("Matrícula:", aluno.matricula)
                print("Nome:", aluno.nome)
                print("Situação:", aluno.situacao)
                print("Nota final:", aluno.nota_final)

            else:
                print("Aluno não encontrado.")

        elif opcao == 6:
            matricula = int(input("Digite a matrícula: "))
            nova_nota = float(input("Digite a nova nota: "))
            alterar_nota(lista,matricula,nova_nota)

        elif opcao == 7:
            matricula = int(input("Digite a matrícula: "))
            alterar_situacao(lista,matricula)

        elif opcao == 8:
            matricula = int(input("Digite a matrícula: "))
            lista = remover(lista,matricula)

        elif opcao == 9:

            quantidade = quantidade_alunos(lista)
            print("Quantidade de alunos:", quantidade)
 
        elif opcao == 10:
            media = media_turma(lista)
            print("Média da turma:", media)

       
        elif opcao == 11:
            media = media_ativos(lista)
            print("Média dos alunos ativos:", media)

        elif opcao == 12:

            print("Programa encerrado.")
        else:
            print("Opção inválida!")


main()
