def minToHor(min):
    hor = min//60
    min -= hor*60

    return hor, min

def main():
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
        horas, minutos = minToHor(tMinu)

        print(f"Tempo da corredora: {horas:02d}h {minutos:02d}min")
    else:
        horas, minutos = minToHor(tMinu)

        print(f"Tempo do corredor: {horas:02d}h {minutos:02d}min")

    horas, minutos = minToHor(tMax)

    print(f"Tempo necessario: {horas:02d}h {minutos:02d}min")

    tempo = tMax - tMinu

    if (tempo >= 0 and (sexob == "m" or sexob == "M")):
        print("Conseguiu indice? SIM")
        horas, minutos = minToHor(tempo)
        print(f"O corredor correu {horas:02d}h {minutos:02d}min abaixo do indice")
    elif (tempo >= 0 and (sexob == "f" or sexob == "F")):
        print("Conseguiu indice? SIM")
        horas, minutos = minToHor(tempo)
        print(f"A corredora correu {horas:02d}h {minutos:02d}min abaixo do indice")
    elif (tempo < 0 and (sexob == "m" or sexob == "M")):
        print("Conseguiu indice? NAO")
        horas, minutos = minToHor(abs(tempo))
        print(f"O corredor correu {horas:02d}h {minutos:02d}min acima do indice")
    elif (tempo < 0 and (sexob == "F" or sexob == "f")):
        print("Conseguiu indice? NAO")
        horas, minutos = minToHor(abs(tempo))
        print(f"A corredora correu {horas:02d}h {minutos:02d}min acima do indice")

main()