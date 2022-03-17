def populate(qnt, lista, i = 1):
    if (qnt >= i):
        lista[i] = input()
        return populate(qnt, lista, i + 1)
    return lista

def populateVts(qnt, lista, i = 1):
    if (qnt >= i):
        vt = int(input())
        lista[vt if (vt <= (len(lista) - 1)) else -1] += 1
        return populateVts(qnt, lista, i + 1)
    return lista

def win(listaV, pMaior = 1, maior = 0, i = 1):
    if ((len(listaV) - 1) > i):
        if (listaV[i] > maior):
            return win(listaV, i, listaV[i], i + 1)
        return win(listaV, pMaior, maior, i + 1)
    return pMaior

def printR(listaC, listaV, W, i = 1):
    if ((len(listaC) - 1) > i):
        print(f"{listaC[i]}: {listaV[i]}")
        printR(listaC, listaV, W, i + 1)
    else:
        print(f"{listaC[0]}: {listaV[0]}")
        print(f"{listaC[-1]}: {listaV[-1]}")
        print(f"Vencedor(a): {listaC[W]}")
        return

def main ():
    nCan = int(input())
    lN = ["Brancos"] + [""] * nCan + ["Nulos"]
    lN = populate(nCan, lN[:])

    nVts = int(input())
    lV = [0] * len(lN)
    lV = populateVts(nVts, lV[:])

    printR(lN, lV, win(lV))

main()