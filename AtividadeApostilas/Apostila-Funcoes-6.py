""" #E1
from math import pi

def main():
    r = float(input());
    a, v = esfera(r);

    print(f"Area: {a};\nVolume: {v}.");

def esfera(r):
    a = 4 * pi * (r**2);
    v = (4 * pi * (r**3)) / 3;

    return a, v;
    
main();
"""

#""" #E2 e E3
def main():
    v1 = float(input());
    v2 = float(input());
    v3 = float(input());

    maiorv = maior(v1, v2);
    maiorv3 = maior3(v1, v2, v3);

    print(f"Maior: {maiorv}.");
    print(f"Maior3: {maiorv3}.");

def maior(v1, v2):
    return v1 if (v1>=v2) else v2;

def maior3(v1, v2, v3):
    return v1 if (v2 <= v1 >= v3) else v2 if (v1 <= v2 >= v3) else v3;

main();
#"""