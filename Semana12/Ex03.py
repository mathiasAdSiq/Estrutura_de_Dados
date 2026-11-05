def mostrar_valor(n):
    if n == 1:
        print(n)
        return (1)

    print(n)
    return n + mostrar_valor(n - 1)


soma = mostrar_valor(6)
print('SOMA:', soma)


#Sequência de chamadas
#soma(6) = 6 + soma(5)
#soma(5) = 5 + soma(4)
#soma(4) = 4 + soma(3)
#soma(3) = 3 + soma(2)
#soma(2) = 2 + soma(1)
#soma(1) = 1

#Sequência de retornos
#soma(1) = 1
#soma(2) = 2 + 1 = 3
#soma(3) = 3 + 3 = 6
#soma(4) = 4 + 6 = 10
#soma(5) = 5 + 10 = 15
#soma(6) = 6 + 15 = 21
