
n = int(input("Digite o número: "))

def mostar_valor(n):
    if n == 0:
        return 

    if n % 2 == 0:
        
        print("somente pares:", n)
    mostar_valor(n - 1)
    
mostar_valor(n)
