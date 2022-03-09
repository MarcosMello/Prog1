def soma1(L, i = 0):
    #Implemente a função usando a variável 'i' para controlar
    #o número de vezes que a função será chamada recursivamente
    if len(L) == i:
        return 0

    return L[i] + soma1(L, i + 1)

def soma2(L):
    if len(L) == 0:
        return 0
    return L[0] + soma2(L[1:])

def main():
    print("Soma1: ", soma1(list(range(1, 100))))
    print("Soma2: ", soma2(list(range(1, 100))))

main()