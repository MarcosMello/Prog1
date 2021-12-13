from math import pi

def areaEsfera1():
    raio = float(input("Raio: "))

    print(f"Area da Esfera: {4*pi*(raio**2)}")

def areaEsfera2(raio):
    print(f"Area da Esfera: {4*pi*(raio**2)}")

def areaEsfera3(raio):
    return 4*pi*(raio**2)

def main():
    areaEsfera1()

    raio2 = float(input("Insira o raio: "))
    areaEsfera2(raio2)

    raio3 = float(input("Insira o raio: "))
    area3 = areaEsfera3(raio3)

    print(f"Area3: {area3}")

main()
