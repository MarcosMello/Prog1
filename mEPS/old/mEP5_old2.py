######################################################
# Programação Funcional / Programção I (2021/2)
# miniEP5 - Jogo da Velha
# Nome: Marcos Vinicius Vargas Mello
# Matrícula: 2021200102
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional.
# - Você não pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Você deve seguir o código base disponibilizado, 
#   não sendo permitido a alteração do nome e/ou
#   lista de parâmetros das funções dadas;
# - Caso precise, você PODE criar outras funções;
# - Não é permitido a utilização de lista, tuplas 
#   ou qualquer outro tipo estruturado para 
#   “facilitar” a manipulação dos dados. Você deve 
#   sempre trabalhar com as 9 variáveis que 
#   representam as posições no tabuleiro;
#
# Dica: Leia o docstring de cada função para saber o
#       que cada uma deve fazer e retornar.
######################################################

def countS(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    x, o, s = 0, 0, 0 

    f = lambda p, x, o, s: ((x + 1, o, s) if (p == "x") else (x, o + 1, s) if (p == "o") else (x, o, s)) if (p != " ") else (x, o, s + 1)

    x, o, s = f(p1, x, o, s)
    x, o, s = f(p2, x, o, s)
    x, o, s = f(p3, x, o, s)
    x, o, s = f(p4, x, o, s)
    x, o, s = f(p5, x, o, s)
    x, o, s = f(p6, x, o, s)
    x, o, s = f(p7, x, o, s)
    x, o, s = f(p8, x, o, s)
    x, o, s = f(p9, x, o, s)

    return x, o, s

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9): #vf
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    print(f" {p7} | {p8} | {p9} ")
    print("---+---+---")
    print(f" {p4} | {p5} | {p6} ")
    print("---+---+---")
    print(f" {p1} | {p2} | {p3} ")

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    x, o, s = countS(p1, p2, p3, p4, p5, p6, p7, p8, p9)

    return True if ((x + o + s) == 9) else False

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9): #vf
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    x, o, s = countS(p1, p2, p3, p4, p5, p6, p7, p8, p9)

    return False if (abs(x - o) >= 2) else True

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    x, o, s = countS(p1, p2, p3, p4, p5, p6, p7, p8, p9)

    f = lambda p, pl, pll: True if ((p != " ") and (pl != " ") and (pll != " ")) else False

    if (f(p1, p2, p3) and (p1 == p2 == p3)): #- # da pra fazer uma função lamda que usa a outra, passaremos p1, p2, p3 ...
        print(f"O jogador '{p1}' venceu!")    
    elif (f(p4, p5, p6) and (p4 == p5 == p6)): #-
        print(f"O jogador '{p4}' venceu!")
    elif (f(p7, p8, p9) and (p7 == p8 == p9)): #-
        print(f"O jogador '{p7}' venceu!")
    elif (f(p7, p4, p1) and (p7 == p4 == p1)): #|
        print(f"O jogador '{p7}' venceu!")
    elif (f(p8, p5, p2) and (p8 == p5 == p2)): #|
        print(f"O jogador '{p8}' venceu!")
    elif (f(p9, p6, p3) and (p9 == p6 == p3)): #|
        print(f"O jogador '{p9}' venceu!")
    elif (f(p7, p5, p3) and (p7 == p5 == p3)): #\
        print(f"O jogador '{p7}' venceu!")
    elif (f(p1, p5, p9) and (p1 == p5 == p9)): #/
        print(f"O jogador '{p1}' venceu!")
    else:
        if (s >= 1):
            print("O jogo nao terminou!")
        else:
            print("Empate!")

######################################################
##            NÃO ALTERE A FUNÇÃO 'main'            ##
######################################################
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()