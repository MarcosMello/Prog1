def div():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f"{numero} é divisivel por 2.")
        return 1
    else:
        print(f"{numero} não é divisivel por 2.")
        return 0
    
def main():
    contador = 0

    contador += div()
    contador += div()
    contador += div()
    contador += div()
    contador += div()

    print(f"Temos {contador} números divisiveis por 2.")

main()