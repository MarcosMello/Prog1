from math import pi

def main():
    esfera();

def esfera():
    r = float(input());

    a = 4 * pi * (r**2);
    v = (4 * pi * (r**3)) / 3;

    print(f"Area: {a};\nVolume: {v}.");
    
main();