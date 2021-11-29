media = float(input("Digite a média do aluno: "));

if 0 <= media <= 10:
    if media >= 9.0:
        print("A");
    elif media >= 8.0:
        print("B");
    elif media >= 7.0:
        print("C");
    elif media >= 6.0:
        print("D");
    else:
        print("R");
else:
    print("Erro");
