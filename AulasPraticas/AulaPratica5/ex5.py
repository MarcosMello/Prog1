def divisivel(x, y):
    return 0 if (x%y == 0) else 1

def main():
    x = float(input("Digite um numero: "))
    y = float(input("Digite outro: "))
    div = divisivel(x, y)

    print("Divisivel") if (div == 0) else print("Nao divisivel")

main()