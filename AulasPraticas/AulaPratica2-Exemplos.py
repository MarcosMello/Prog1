""" -> Exemplo 1
nota1 = 8; # Nota da Prova 1
nota2 = 7.5; # Nota da Prova 2
nota3 = 8.2; # Nota da Prova 3
media = (nota1 + nota2 + nota3) / 3.0;
print(f"Média = {media:.2f}");
if media < 7.0:
    print("\nAluno de prova final\n");
else:
    print("\nAluno aprovado\n");
"""
""" -> Exemplo 2
     #Erro: O IF está atribuindo e não verificando se é igual; X não está sendo convertido para int.
     #Pergunta 1: Sim, poderia, pois é algo contrario a primeira opção.
     #Pergunta 2: Não, não poderia, pois é algo totalmente diferente do IF que o precede.
x = int(input("Digite um número: "));
if x%2 == 0:
    print(f"{x} é par.");
if x%2 == 1:
    print(f"{x} é impar.");
if x%2 == 0 or x%3 == 0:
    print(f"{x} é divisivel por 2 ou 3.");
if x%2 == 0 and x%5 == 0:
    print(f"{x} é divisivel por 2 e 5, logo é algum numero multiplo de 10.");
"""
#""" -> Exemplo 3
     #Erros: Falta dois pontos depois dos IFs; A Variavel média não foi criada; Identação;
media = float(input("Insira a media: "));

if media >= 9.0:
    print("A");
else:
    if media >= 8.0:
        print("B")
    else:
        if media >= 7.0:
            print("C")
        else:
            if media >= 6.0:
                print("D")
            else:
                print("R")
#"""