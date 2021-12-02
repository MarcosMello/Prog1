lado1 = int(input());
lado2 = int(input());
lado3 = int(input());

if (lado1 <= 0 or lado2 <= 0 or lado3 <= 0): #negativo ou 0
    print("Valores invalidos.");
elif (lado1 >= (lado2 + lado3) or lado2 >= (lado3 + lado1) or lado3 >= (lado1 + lado2)): #lado maior que soma
    print("Valores nao podem formar um triangulo.");
else:
    if (lado1 == lado2 and lado1 == lado3): #todos lados iguais
        print("Triangulo equilatero.");
    elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3): #dois lados iguais
        print("Triangulo isosceles.");
    else: #todos diferentes
        print("Triangulo escaleno.");
    
    if (lado2 < lado1 > lado3): #se lado1 for o maior
        maior = lado1;
        outro1 = lado2;
        outro2 = lado3;
    elif (lado1 < lado2 > lado3): #se lado2 for o maior
        maior = lado2;
        outro1 = lado1;
        outro2 = lado3;
    elif (lado1 < lado3 > lado2): #se lado3 for o maior
        maior = lado3;
        outro1 = lado1;
        outro2 = lado2;
    else: #se forem iguais, uma vez que o equilatero sempre tem seus angulos/lados iguais
        maior = lado1;
        outro1 = lado2;
        outro2 = lado3;
        #ou print("Triangulo acutangulo.");

    if ((maior**2) < (outro1**2 + outro2**2)): #formula acutangulo
        print("Triangulo acutangulo.");
    elif ((maior**2) == (outro1**2 + outro2**2)): #formula retangulo
        print("Triangulo retangulo.");
    elif ((maior**2) > (outro1**2 + outro2**2)): #formula obtusangulo
        print("Triangulo obtusangulo.");