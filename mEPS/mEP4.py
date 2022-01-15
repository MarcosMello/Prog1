def minToHor(min):
    hor = min//60
    min -= hor*60

    return f"{hor:02d}h {min:02d}min"

def corredor(mulher, frs):
    txt = ("da" if (mulher) else "do") if (frs) else ("A" if (mulher) else "O")

    return f"{txt} {('corredora' if (mulher) else 'corredor')}"

def main():
    mulher = False

    tMinu = int(input())
    idade = int(input())
    sexob = input()

    f = lambda idade, i, m: (m * (idade//5 - i//5))

    if idade < 34:
        tMax = 180
    elif idade >= 80:
        tMax = 290
    elif idade <= 54:
        tMax = (180 if idade <= 44 else 180 + 5) + (f(idade, 34, 5))
    else:
        tMax = 215 + (f(idade, 59, 15))
    
    mulher = True if (sexob == "f" or sexob == "F") else False
    tMax += 30 if (mulher) else 0
    
    print(f"Tempo {corredor(mulher, True)}: {minToHor(tMinu)}")

    print(f"Tempo necessario: {minToHor(tMax)}")

    tempo = tMax - tMinu

    acOrAb, indice = ("abaixo" if tempo >= 0 else "acima"), ("SIM" if tempo >= 0 else "NAO")  

    print(f"Conseguiu indice? {indice}")

    print(f"{corredor(mulher, False)} correu {minToHor(abs(tempo))} {acOrAb} do indice")

main()