def ang(maior, outro1, outro2):
    if ((maior**2) < ((outro1**2) + (outro2**2))):
        print("Triangulo acutangulo.");
    elif ((maior**2) == ((outro1**2) + (outro2**2))):
        print("Triangulo retangulo.");
    elif ((maior**2) > ((outro1**2) + (outro2**2))):
        print("Triangulo obtusangulo.");

def tri(l1, l2, l3):
    if (l1 == l2 and l1 == l3):
        print("Triangulo equilatero.");
    elif ((l1 == l2) or (l2 == l3) or (l1 == l3)):
        print("Triangulo isosceles.");
    else:
        print("Triangulo escaleno.");

l1 = int(input());
l2 = int(input());
l3 = int(input());

if ((l1 >= l2 + l3) or (l2 >= l1 + l3) or (l3 >= l1 + l2)):
    print("Valores nao podem formar um triangulo.");
elif (l1 <= 0 or l2 <= 0 or l3 <= 0):
    print("Valores invalidos.");
else:
    if (l1 > l2 and l1 > l3): #200,250,300
        tri(l1, l2, l3);
        ang(l1, l2, l3);
    elif (l2 > l1 and l2 > l3):
        tri(l1, l2, l3);
        ang(l2, l1, l3);
    elif (l3 > l1 and l3 > l2):
        tri(l1, l2, l3);
        ang(l3, l1, l2);
    else:
        tri(l1, l2, l3);
        print("Triangulo equilatero.");