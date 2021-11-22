""" -> Exercicio 1
     #Pergunta: Não, apresenta erros: 0 -> Negativo, como corrigir? x >= 0. Gera 1 eh positivo.
     #Correçoes: "f{x} é positivo" e x >= 0
x = int(input("Insira: "));

if x >= 0:
    print(f"{x} é positivo");
else:
    print(f"{x} é negativo");
"""
""" -> Exercicio 1 OBI

d = int(input("Distancia: "));

if (d <= 800):
    print(1);
else:
    if (d > 800 and d <= 1400):
        print(2);
    else:
        if (d > 1400 and d <= 2000):
            print(3);
        else:
            print("Erro");

"""
""" -> Exercicio 2 OBI

a = int(input("A: "));
b = int(input("B: "));
c = int(input("C: "));

if (0 <= a <= 100 and 0 <= b <= 100 and 0 <= c <= 100):
    if (a == b):
        print(c)
    else:
        if (a == c):
            print(b);
        else:
            if (b == c):
                print(a);
            else:
                print("ERRO");
else:
    print("ERRO");

"""
#""" -> Exercicio 3 OBI

l = int(input("L: "));
c = int(input("C: "));

if (1 <= l <= 1000 and 1 <= c <= 1000):
    if(l % 2 == 1 and c % 2 == 1):
        print(1);
    else:
        if (l % 2 == 0 and c % 2 == 1):
            print(0);
        else:
            if (l % 2 == 1 and c % 2 == 0):
                print(0);
            else:
                if (l % 2 == 0 and c % 2 == 0):
                    print(1);

#"""