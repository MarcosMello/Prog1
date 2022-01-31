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

def countXO(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    x = o = 0

    f = lambda p: None if p == " " else True if p == "x" else False

    resp = f(p1)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1
    
    resp = f(p2)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1
    
    resp = f(p3)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1
    
    resp = f(p4)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1
    
    resp = f(p5)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1
    
    resp = f(p6)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1
    
    resp = f(p7)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1
    
    resp = f(p8)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1
    
    resp = f(p9)

    if resp == True:
        x += 1
    elif resp == False:
        o += 1

    return x, o

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
    if   (p1 != " " and p1 != "x" and p1 != "o"):#talvez transformar em func seria ok?
        return False
    elif (p2 != " " and p2 != "x" and p2 != "o"):
        return False
    elif (p3 != " " and p3 != "x" and p3 != "o"):
        return False
    elif (p4 != " " and p4 != "x" and p4 != "o"):
        return False
    elif (p5 != " " and p5 != "x" and p5 != "o"):
        return False
    elif (p6 != " " and p6 != "x" and p6 != "o"):
        return False
    elif (p7 != " " and p7 != "x" and p7 != "o"):
        return False
    elif (p8 != " " and p8 != "x" and p8 != "o"):
        return False
    elif (p9 != " " and p9 != "x" and p9 != "o"):
        return False
    else:
        return True

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9): #vf
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    x, o = countXO(p1, p2, p3, p4, p5, p6, p7, p8, p9)

    return False if (abs(x - o) >= 2) else True

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    f = lambda p, pl, pll: True if ((p != " ") and (pl != " ") and (pll != " ")) else False

    if (f(p1, p2, p3) and (p1 == p2 == p3)): #-
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
        if ((p1 == " ") or (p2 == " ") or (p3 == " ") or (p4 == " ") or (p5 == " ") or (p6 == " ") or (p7 == " ") or (p8 == " ") or (p9 == " ")):
            print("O jogo nao terminou!")
        else:
            print("Empate!")

######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
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