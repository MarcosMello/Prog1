def divisores(n, L=[], i=1):
    if i <= n:
        if n % i == 0:
            return divisores(n, L + [i], i + 1)
        else:
            return divisores(n, L, i + 1)
    else:
        return L

def listaPrimos(n, L = [], i = 2):
    if len(L) != n:
        if len(divisores(i)) == 2:
            return listaPrimos(n, L + [i], i + 1)
        return listaPrimos(n, L, i + 1)
    return L

def main():
    print(listaPrimos(5))
    print(listaPrimos(10))
    L = listaPrimos(15)
    print([x**2 for x in L]) #Elevar todos os itens de L por 2

main()