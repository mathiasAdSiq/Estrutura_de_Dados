

class No:
    def __init__(self,matricula,nome,situacao,nota_final):
        self.matricula = matricula
        self.nome = nome
        self.situacao = True
        self.nota_final = nota_final
        self.proximo = None

    def menu():
        print("1 - cadastrar um aluno no final da lista;")
        print("2 - Listar todos os alunos cadastrados;")
        print("3 - Listar apenas alunos ativos no sistema;")
        print("4 - Listar apenas alunos desativados no sistema;")
        print("5 - Buscar um aluno pela matrícula;")
        print("6 - Alterar nota final de um aluno;")
        print("7 - Alterar a situação do aluno (True -> False ou False ->True)")
        print("8 - Remover um aluno da lista;")
        print("9 - Informar a quantidade de alunos cadastrados;")
        print("10 - Calcular a média das notas da turma;")
        print("11 - Calcular a média das notas dos alunos ativos no sistema.")
        print("12 - Sair.")

        opcao = int(input("Digite a sua opção: "))

        return opcao

    def cadastrar_final(lista, matricula, nome, situacao, nota_final):
        novo = No(matricula, nome, situacao, nota_final)
         
        
        if lista == None:
            return novo
        aux = lista
   
        while aux != None:

            aux = aux.proximo

        return lista
           
            
    def listar_alunos_cadastratos(lista):
        if lista is None:
            print("Lista vazia")
            return

        while aux is not None:
            print("Matricula:", aux.matricula)
            print("Nome:", aux.nome)
            print("Situação:", aux.situacao)
            print("Nota Final:", aux.nota_final)
 
            aux = aux.proximo

    def listar_alunos_ativos(lista):
        if lista is None:
            print("Lista vazia")
            return

        aux = lista
        encontrou = False

        while aux is not None:
            if aux.situacao == True:
                print("Matricula:", aux.matricula)
                print("Nome:", aux.nome)
                print("Situação:", aux.situacao)
                print("Nota Final:", aux.nota_final)
            encontrou = True

        aux = aux.proximo

        if encontrou == False:
            print("Não existem alunos desativados.")

    def listar_alunos_desativos(lista,matricula):
        aux = lista

        while aux is not None:
            if aux.matricula == matricula:
                print("-------------------------")
                print("Matrícula:", aux.matricula)
                print("Nome:", aux.nome)
                print("Situação:", aux.situacao)
                print("Nota final:", aux.nota_final)
                return aux

            aux = aux.proximo

        print("Aluno não encontrado.")
        return None
            
    def buscar(lista,matricula):
        a =1 

def main():
    lista = None
    opcao = 0

    while opcao != 12:

        opcao = menu()

        if opcao == 1:    
            matricula = int(input("Digite o numero de matricula do aluno:"))
            nome = input("Digite o nome do aluno:")
            nota_final = int(input("Digite a nota final do aluno"))

            lista = cadastrar_final(
                lista,
                matricula,
                nome,
                nota_final
            )

            print("Aluno cadastrado com sucesso!")

        elif opcao == 2:
                listar_alunos_cadastratos(lista)

        elif opcao == 3:
            listar_alunos_ativos(lista)
            
        elif opcao == 4:
            listar_alunos_desativos(lista)

        elif opcao == 5:
            matricula = int(input("Digite o numero da matricula do aluno a ser buscado: "))
            buscar(lista, matricula)

            #elif opc == 6:
                

            #elif opc == 7:


main()
