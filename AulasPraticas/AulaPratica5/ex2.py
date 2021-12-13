def soma3(x, y):
    return x + y
    print("Chegou aqui!")
    #chegou aqui não é impressa pois acontece depois do return, que é onde a função é finalizada

def main():
    x = float(input("Digite um numero: "))
    y = float(input("Digite outro: "))
    soma = soma3(x, y)

    print(f"Soma: {soma}")

main()