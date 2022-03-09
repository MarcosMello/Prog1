def funcao1(L, i = 0, R = []):
    if i == len(L):
        return R
    else:
        print(f"L[0] = {L[0]} L = {L} R = {R}")
        if L[i] in R:
            return funcao1(L, i + 1, R)
        else:
            return funcao1(L, i + 1, R + [L[i]])


def funcao2(L, R=[]):
    if len(L) == 0:
        return R
    else:
        print(f"L[0] = {L[0]} L = {L} R = {R}")
        if L[0] in R:
            return funcao2(L[1:], R)
        else:
            return funcao2(L[1:], R + [L[0]])

def main():
    #O Objetivo é fazer uma função que rejeita itens duplicados

    print("Executando 'funcao1([1, 2, 3, 4, 5, 6, 7, 8, 9]'")
    print("Resposta:", funcao1([1, 2, 3, 4, 5, 6, 7, 8, 9]), "\n")

    print("Executando 'funcao2([1, 2, 3, 4, 5, 6, 7, 8, 9]'")
    print("Resposta:", funcao2([1, 2, 3, 4, 5, 6, 7, 8, 9]), "\n")

    print("Executando 'funcao1([0, 1, 0, 1, 0, 1, 2, 3, 2, 4])'")
    print("Resposta:", funcao1([0, 1, 0, 1, 0, 1, 2, 3, 2, 4]), "\n")

    print("Executando 'funcao2([0, 1, 0, 1, 0, 1, 2, 3, 2, 4])'")
    print("Resposta:", funcao2([0, 1, 0, 1, 0, 1, 2, 3, 2, 4]), "\n")

    print("Executando 'funcao1([1, 1, 1, 1])'")
    print("Resposta:", funcao1([1, 1, 1, 1]), "\n")

    print("Executando 'funcao2([1, 1, 1, 1])'")
    print("Resposta:", funcao2([1, 1, 1, 1]), "\n")

    #Não, pois a primeira está fatiando a lista, enquanto a segunda está apenas sendo iterada.
    #Sim, pois são dois metodos diferentes para fazer a mesma coisa - que é iterar
    # pelos elementos.

    print(funcao1([1, 2, 3], 1)) #[2, 3]; Não, pois, como esse começou pelo segundo
    # item, ele não adicionou o 1 que era necessario.

main()
