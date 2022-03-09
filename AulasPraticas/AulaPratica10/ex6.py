import random
from os import system, name

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "SUA MATRICULA"

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "SEU NOME COMPLETO"

def limpaTela():
	if name == 'nt':
		system('cls')
	else:
		system('clear')
###################################################################################
#(1) Crie uma função que solicite a letra que o jogador deve ser.                 #
# A função retorna dois valores. Se o jogardor desejar ser "X", retorne "X", "O". #
# Caso contrário, retorne "O", "X".                                               #
###################################################################################

###################################################################################
#(2) Crie uma função que dicida/retorna quem será o primeiro a jogar.             #
# Use o módulo random.                                                            #
###################################################################################

###################################################################################
#(3) Crie uma função para imprimir o tabuleiro.                                   #
# Função não retorna nada, apenas imprime.                                        #
###################################################################################

###################################################################################
#(4) Faça uma função que solicite ao usuário onde ele deseja jogar.               #
# A função retorna um inteiro entre 1 e 9 (posisão escolhida)                     #
# A função deve garantir que o usuários selecionou uma posição válida             #
###################################################################################

###################################################################################
#(5) Faça uma função que retorna True se o "X" ou "O" ganhou e False, caso        #
# contrário. A função deve receber o tabuleiro e o simbolo a ser testado.         #
# Verifique todas as possibilidades e retorne True caso uma delas o simbolo       #
# ganhou. Por exemplo, se nas posições 7, 8 e 9 do tabuleiro contém "X",          #
# significa que "X" ganhou e a função deve retornar True.                         #
###################################################################################

###################################################################################
#(6) Faça uma função que retorne True se houve empate e False, caso contrário.    #
# Para isso, basta verificar se o tabuleiro está todo preenchido, ou seja, não    #
# contém nenhum espaço em branco.                                                 #
###################################################################################

###################################################################################
#(7.1) Faça uma função que receba o tabuleiro e retorne as posições, entre 1 e 9  #
# que estão livres                                                                #
###################################################################################
###################################################################################
#(7.2) Faça uma função que receba o tabuleiro, escolha (aleatoriamente) e retorne #
# uma posição livre. Use a função (7.1).
###################################################################################

###################################################################################
#(8) Começa a implementar a função jogadaComputador. De início, você pode apenas  #
# sortear uma posição livre como sendo a jogada do computador. Use a função (7.2) #
# Posteriormente, implemente alguma estratégia mais  "inteligente".               #
###################################################################################
def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas,
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador
    """
    return

###################################################################################
#(9) Faça uma função que será responsável pelas jogadas, intercalando entre o     #
# jogador e o computador. Essa função, caso queira, pode retornar quem venceu ou  #
# se o jogo terminou empatado. Note que essas função deve ser recursiva, ou seja, #
# ela deve ser chamada recursivamente para cada jogada enquanto não houver        #
# vencedor ou empate.                                                             #
# Sugestão de parâmetros obrigatórios para essa fução:                            #
# - Tabuleiro                                                                     #
# - De quem é a vez da jogada                                                     #
# - Simbolo do jogador                                                            #
# - Simbolo do computador                                                         #
###################################################################################



def main():
    limpaTela()
    #(10) Mensagem de boas-vindas :)

    #(11) Cria o tabuleiro (uma lista de tamanho 10, inicialmente vazia).
    # Escolha algum simbolo para representar que determinada posição está vazia.
    # Minha sugestão é "" ou " ", mas sinta-se a vontade para escolher o simbolo
    # que achar melhor.

    #(12) Chame a função (1) e atribua o resultado a duas variáveis. Uma irá representar
    # o simbolo do jogador e a outra o simbolo do computador.

    #(13) Chame a função (2) e atribua o resultado a um variável que representa quem
    # começa jogando.
    # Imprima quem irá começar a partida.

    #(14) Chame a função (9)

if __name__ == "__main__":
    main()