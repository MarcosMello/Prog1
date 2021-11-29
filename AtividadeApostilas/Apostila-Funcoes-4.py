def soma1 ():
    x = float(input("Digite um número: "));
    y = float(input("Digite outro: "));
    return x + y;

def soma2 (x, y):
    return x + y;

s1 = soma2(2, 3);
print(f"S2 = {soma1()}");

print(f"A soma de 1 + 2 é {soma2(1, 2)}.");
print(f"S1 = Soma de 2 + 3 = {s1}");