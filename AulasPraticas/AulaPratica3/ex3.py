jogador1 = input("Você quer ser X ou O? ");

if jogador1 == "X":
    jogador2 = "O";
    print(f"Jogador 1 escolheu {jogador1} e o Jogador 2 ficou com {jogador2}.");
elif jogador1 == "O":
    jogador2 = "X";
    print(f"Jogador 1 escolheu {jogador1} e o Jogador 2 ficou com {jogador2}.");
else:
    print("ERRO");
