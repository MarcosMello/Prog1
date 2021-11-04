#Exemplo
"""
categoria = int(input("Digite a categoria do produto: "));
preco = 0;

if categoria == 1:
    preco = 10;
else:
    if categoria == 2:
        preco = 18;
    else:
        if categoria == 3:
            preco = 23;
        else:
            if categoria == 4:
                preco = 26;
            else:
                if categoria == 5:
                    preco = 31;
                else:
                    print("Categoria inválida!");

print(f"O preço do produto é: R$ {preco}");
"""
#Primeira Tarefa
"""
categoria = int(input("Digite a categoria do produto: "));
preco = 0;

if categoria == 1:
    preco = 10;
else:
    if categoria == 2:
        preco = 18;
    else:
        if categoria == 3:
            preco = 23;
        else:
            if categoria == 4:
                preco = 26;
            else:
                if categoria == 5:
                    preco = 31;
                else:
                    print("Categoria inválida!");

if preco:
    print(f"O preço do produto é: R$ {preco}");
"""
#Segunda Tarefa - v1
#"""
categoria = int(input("Digite a categoria do produto: "));
preco = 0;

if categoria == 1:
    preco = 10;
if categoria == 2:
    preco = 18;
if categoria == 3:
    preco = 23;
if categoria == 4:
    preco = 26;
if categoria == 5:
    preco = 31;
if categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4 and categoria != 5:
    print("Categoria inválida!");

if preco:
    print(f"O preço do produto é: R$ {preco}");
#"""