
#for i in range(5, 1 ,-1):
#    print(i)


def mostrar_valor(n):
    if n < 0:
        return 0
    print(n)
    return n + mostrar_valor(n - 1)
    #print("Pós-recursividade:", n)


soma = mostrar_valor(5)
print('SOMA:', soma)
