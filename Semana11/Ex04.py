
def recursiva(n):
    if n == 0:
        return
    print("Caixas:",n)
    recursiva(n - 1)

recursiva(10)
