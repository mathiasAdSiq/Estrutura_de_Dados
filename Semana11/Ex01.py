def contagen_regressiva(n):
    if n == 11:
        return 0
    
    contagen_regressiva(n +1)
    print("Contagem regresiva:", n)

contagen_regressiva(1)
