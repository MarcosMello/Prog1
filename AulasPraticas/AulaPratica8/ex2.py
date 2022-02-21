def imprime(L, i = 0):
    if i < len(L):
        if (L[i] % 2 == 0):
            print(L[i])
        imprime(L, i + 1)

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    imprime(lista)

main()