import random as r

def megaSena(n1, n2, n3, n4, n5, n6, i = 0):
    if i <= 6:
        s = r.randint(1, 60)

        if s != n1 and s != n2 and s != n3 and s != n4 and s != n5 and s != n6:
            return 0 + megaSena(n1, n2, n3, n4, n5, n6, i + 1)
        else:
            return 1 + megaSena(n1, n2, n3, n4, n5, n6, i + 1)
    
    return 0
    
def teste(n, n1, n2, n3, n4, n5, n6, menor = 6, maior = 0, acertos = 0, i = 0):
    if n == 1 or n % 2:
        a = megaSena(n1, n2, n3, n4, n5, n6)
        return (a, a, a/(6 * n)) if (n == 1) else teste(n - 1, n1, n2, n3, n4, n5, n6, (a if (a < menor) else menor), (a if (a > maior) else maior), acertos + a, i)

    else:
        if (n >= i):
            a = megaSena(n1, n2, n3, n4, n5, n6)
            a2 = megaSena(n1, n2, n3, n4, n5, n6)
            menor = (a if (a < menor) else menor)
            maior = (a if (a > maior) else maior)
        
            return teste(n, n1, n2, n3, n4, n5, n6, menor, maior, acertos + a + a2, i + 2)

        return menor, maior, acertos/(6 * n)

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    n6 = int(input())
    if 1 < n1 > 60 or 1 < n2 > 60 or 1 < n3 > 60 or 1 < n4 > 60 or 1 < n5 > 60 or 1 < n6 > 60:
        print("ERRO!")
    else:
        #print(f"Acertou {megaSena(n1, n2, n3, n4, n5, n6)} numeros de 6.")
        n = int(input())
        if 1 < n > 1000:
            print("ERRO!")
        else:
            menor, maior, media = teste(n, n1, n2, n3, n4, n5, n6)
            print(f"Teste -> Menor: {menor}, Maior: {maior}, Media: {media}")

main()

#nos meus testes, em nenhuma chance o jogador acertou todos os 6 numeros.
#Com menor:0, maior:4, a média foi 0.117.