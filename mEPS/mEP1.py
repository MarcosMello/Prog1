x = float(input());
y = float(input());

if (x == 0 or y == 0):
    print("EIXOS"); #adicionei porque estava no pdf
else:
    if (x > 0 and y > 0):
        print("I");
    elif (x < 0 and y > 0):
        print("II");
    elif (x < 0 and y < 0):
        print("III");
    elif (x > 0 and y < 0): #aqui tambem poderia ser usado else
        print("IV");