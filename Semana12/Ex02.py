
def mostrar_valor(n):
    if n < 0:
        return 0
    print(n)
    return mostrar_valor(n - 1)
    #print("Pós-recursividade:", n)

mostrar_valor(5)
