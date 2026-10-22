
n = int(input("Digite o número: "))

def soma_pares(n, soma= 0):
    if n == 0:
        print("soma dos impares: ",soma)
        return 

    if n % 2 != 0:
        soma += n
        print("somente impares:", n)
    soma_pares(n - 1,soma)
    
soma_pares(n)
