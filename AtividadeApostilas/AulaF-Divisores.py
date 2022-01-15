def div(n = 1, c = 0):
    if (n > 0): 
        numero = int(input("Digite um número: "))

        if numero % 2 == 0:
            print(f"{numero} é divisivel por 2.")
            c += 1
        else:
            print(f"{numero} não é divisivel por 2.")
            c += 0
        
        return div(n-1, c)
    else:
        return c
    
def main():
    n = int(input())
    print(f"Temos {div(n)} números divisiveis por 2.")

main()