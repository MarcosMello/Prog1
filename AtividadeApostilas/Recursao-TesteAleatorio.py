def rec():
    x = int(input("Insira um valor valido: "))
    if x < 0:
        return(rec());
    else:
        return x

def main():
    x = int(input("Insira um valor: "))
    if x < 0:
        x = rec()
        print(f"Agora sim! Ok, {x}")
    else:
        print(f"Ok, {x}")

main()