from math import pi

def volumeCilindro(raio, altura):
    if (isinstance(raio, (int, float)) and isinstance(altura, (int, float))):
        return pi*(raio**2)*altura

def main():
    r = float(input("Digite o raio: "))
    h = float(input("Digite a altura: "))
    volume = volumeCilindro(r, h)
    print(f"O volume e: {volume}")

    volume2 = volumeCilindro("x", h)
    print(f"O volume e: {volume2}")

main()