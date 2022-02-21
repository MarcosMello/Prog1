def imprimeResultado(lista, i = 0):
    if i < len(lista):
        print(f"{i:02d}: [{lista[i]:02d}] {'*'*lista[i]}")
        imprimeResultado(lista, i + 1)

def contaValoresLidos(n, L = [0]*11, valoresValidos = 0, i = 0): #11 pois é de 0 a 10, temos 11 números nesse intervalo
    """
    Faz a leitura de n valores inteiros e contabiliza a quantidade de 
    vezes que os números entre 0 e 10 foram lidos. Após a leitura, a 
    função deve retornar:
    - A lista L conténdo, na posição i, a quantidade de vezes
    que o valor i foi digitado e;
    - A quantidade de valores válidos lidos.
    """
    if i < n:
        #valor = int(input("Digite um valor: "))
        valor = int(input())
        if 0 <= valor <= 10:
            L[valor] += 1
            return contaValoresLidos(n, L, valoresValidos + 1, i + 1)
        else: #Valor não é válido e é ignorado
            #print("Valor inválido!")
            return contaValoresLidos(n, L, valoresValidos, i + 1)

    return L, valoresValidos

def main():
    #n = int(input("Quantos valores serão lidos? "))
    n = int(input())
    resultado, valoresLidos = contaValoresLidos(n)
    print(f"Foram lidos {valoresLidos} valores validos")
    imprimeResultado(resultado)

main()

#Sim, "FC: nenhuma diferença encontrada"