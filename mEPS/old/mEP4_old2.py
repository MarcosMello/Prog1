def minToHor(min):
    hor = min//60
    min -= hor*60

    return hor, min

def main():
    runner = "corredor"
    runner_art = "do"
    runner_art2 = "O"

    tMinu = int(input())
    idade = int(input())
    sexob = input()

    if (idade <= 34):
        tMax = 180
    elif (idade <= 39):
        tMax = 185
    elif (idade <= 44):
        tMax = 190
    elif (idade <= 49):
        tMax = 200
    elif (idade <= 54):
        tMax = 205
    elif (idade <= 59):
        tMax = 215
    elif (idade <= 64):
        tMax = 230
    elif (idade <= 69):
        tMax = 245
    elif (idade <= 74):
        tMax = 260
    elif (idade <= 79):
        tMax = 275
    else:
        tMax = 290
    
    if (sexob == "f" or sexob == "F"):
        tMax += 30
        runner = "corredora"
        runner_art = "da"
        runner_art2 = "A"
    
    hc, mc = minToHor(tMinu)
    print(f"Tempo {runner_art} {runner}: {hc:02d}h {mc:02d}min")

    hm, mm = minToHor(tMax)
    print(f"Tempo necessario: {hm:02d}h {mm:02d}min")

    tempo = tMax - tMinu

    if tempo >= 0:
        acOrAb = "abaixo"
        indice = "SIM"
    else:
        acOrAb = "acima"
        indice = "NAO"

    print(f"Conseguiu indice? {indice}")

    hf, mf = minToHor(abs(tempo))
    print(f"{runner_art2} {runner} correu {hf:02d}h {mf:02d}min {acOrAb} do indice")

main()