def leitura(soma = 0, qt = 0):
    n = float(input("Digite um valor (um numero <0 indica o fim da leitura): "))
    if n < 0:
        return soma, qt
    else:
        return leitura(soma + n, qt + 1)
    
def main():
    soma, qt = leitura()
    print("Quantidade:", qt)
    print("Soma:", soma)
    if qt > 0:
        print("Média:", soma/qt)

main()