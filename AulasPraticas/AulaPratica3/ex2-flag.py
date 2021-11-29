valido = False;

print("-"*35);
print("101 - Batata List          - R$4.50");
print("305 - Suco Py              - R$2.00");
print("248 - Suco Interpretado    - R$4.25");
print("389 - Guaraná Lambda       - R$3.50");
print("145 - Sanduiche Integral   - R$9.00");
print("567 - Cerveja Derivada     - R$8.50");
print("673 - Vitamina Compilada   - R$7.80");
print("-"*35);

produto = int(input("Escolha seu produto: "));

if produto == 101:
    print("Batata List - R$4.50");
    valido = True;
elif produto == 305:
    print("Suco Py - R$2.00");
    valido = True;
elif produto == 248:
    print("Suco Interpretado - R$4.25");
    valido = True;
elif produto == 389:
    print("Guaraná Lambda - R$3.50");
    valido = True;
elif produto == 145:
    print("Sanduiche Integral - R$9.00");
    valido = True;
elif produto == 567:
    print("Cerveja Derivada - R$8.50");
    valido = True;
elif produto == 673:
    print("Vitamina Compilada - R$7.80");
    valido = True;

if not valido:
    print("ERRO! PRODUTO INVALIDO");