class ContaBancaria:
    def __init__(self, nome, numero_conta, saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo

    def consultar_saldo(self):
        print("Nome do titular:", self.nome)
        print("Número da conta:", self.numero_conta)
        print("Saldo: R$", self.saldo)

    def depositar(self):
        valor = float(input("Valor do depósito: R$ "))

        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
        else:
            self.saldo += valor
            print("Depósito realizado com sucesso!")

        print("Saldo atual: R$", self.saldo)

    def sacar(self):
        saque = float(input("Digite a quantia que deseja sacar: R$ "))

        if saque <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif saque > self.saldo:
            print("Saque não permitido: saldo insuficiente.")
        else:
            self.saldo -= saque
            print("Saque realizado com sucesso!")

        print("Saldo atual: R$", self.saldo)

    def transferir(self, outra_conta):
        valor = float(input("Valor da transferência: R$ "))

        if valor <= 0:
            print("O valor da transferência deve ser maior que zero.")
        elif valor > self.saldo:
            print("Transferência não permitida: saldo insuficiente.")
        else:
            self.saldo -= valor
            outra_conta.saldo += valor
            print("Transferência realizada com sucesso!")

        print("Saldo da conta de origem: R$", self.saldo)
        print("Saldo da conta de destino: R$", outra_conta.saldo)

conta1 = ContaBancaria("João", 1234, 1000)
conta2 = ContaBancaria("Maria", 5678, 500)

while True:

    print("\n===== MENU =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Transferir")
    print("5 - Consultar outra conta")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        conta1.consultar_saldo()

    elif opcao == "2":
        conta1.depositar()

    elif opcao == "3":
        conta1.sacar()

    elif opcao == "4":
        conta1.transferir(conta2)

    elif opcao == "5":
        conta2.consultar_saldo()

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
