def soma1():
    x = float(input("Digite um numero: "))
    y = float(input("Digite outro: "))

    return x+y

def soma2(x, y):
    return x+y

def main():
    soma = soma1()

    x = float(input("Digite um numero: "))
    y = float(input("Digite outro: "))
    somadois = soma2(x, y)

    print(f"A soma da primeira função é: {soma}")
    print(f"A soma da segunda função é: {somadois}")

main()