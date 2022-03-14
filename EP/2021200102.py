######################################################
# Programação Funcional / Programção I (2021/2)
# EP2 - Jogo da Velha
# Nome: Marcos Vinicius Vargas Mello
# Matrícula: 2021200102
######################################################

import random
from os import system, name

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2021200102"

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Marcos Vinicius Vargas Mello"

def limpaTela():
    """
    Função para limpar a tela.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def getPos(f, msg = "", msgE = ["ERRO!", "ERRO!", "ERRO!"]):
    """
    Função responsável pelo input da posição do jogador. - Usa Recursão.

    Parâmetros:
    f (função): Recebe a função de conversão.
    msg (string) (opc): Recebe o texto que vai ser mostrado no input.
    msgE (lista) (string) (opc): Recebe o texto que vai ser mostrado caso tenha um erro.

    Retorno:
    int: Um número de 1-9.
    """
    try: #Tenta converter
        pos = f(input(msg))
        if (1 <= pos <= 9): #Se estiver dentro dos limites pré estabelecidos
            return pos
        print(f"+{'-' * 37}+")
        print(f"|{' ' * 11}{msgE[0]}{' ' * 11}|")
        print(f"|{' ' * 10}{msgE[1]}{' ' * 10}|")
        print(f"|{' ' * 4}{msgE[2]}{' ' * 3}|")
        print(f"+{'-' * 37}+")
        return getPos(f, msg, msgE)
    except: #Se tiver erro chama uma recursão.
        print(f"+{'-' * 37}+")
        print(f"|{' ' * 11}{msgE[0]}{' ' * 11}|")
        print(f"|{' ' * 10}{msgE[1]}{' ' * 10}|")
        print(f"|{' ' * 4}{msgE[2]}{' ' * 3}|")
        print(f"+{'-' * 37}+")
        return getPos(f, msg, msgE)

def xOuO():
    """
    Função que é responsável pelo input do símbolo. - Usa Recursão.

    Retorno:
    ("X", "O"): Se o jogador escolheu o "X".
    ("O", "X"): Se o jogador escolheu o "O".
    """
    symb = input("Você deseja ser 'X' ou 'O'? ")
    if (symb in ["x", "X", "o", "O"]): #Se ele é uma das alternativas aceitaveis
        symb = "X" if (symb in ["x", "X"]) else "O" #Como entrou no if, aqui somente precisamos saber se ele é X, para definir quem o Jogador é e quem o computador é.
        return symb, "X" if (symb != "X") else "O"
    print(f"+{'-' * 37}+")
    print(f"|{' ' * 10}Simbolo inválido!{' ' * 10}|")
    print(f"+{'-' * 37}+")
    return xOuO()

def first(simboloComputador):
    """
    Função que é responsável por decidir quem vai começar.

    Parâmetro:
    simboloComputador (str): Recebe o símbolo do computador.

    Retorno:
    str: Contém quem vai começar jogando.
    """
    c = random.choice(["X", "O"]) #Escolha aleatoria entre "x" e "o"
    print(f"+{'-' * 37}+")
    print(f"|{' ' * 8}O Computador começa!{' ' * 9}|") if (c == simboloComputador) else print(f"|{' ' * 12}Você começa!{' ' * 13}|")
    print(f"+{'-' * 37}+")
    return c

def pTab(tabuleiro, win = [], velha = False):
    """
    Função responsável por imprimir o tabuleiro.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para ser imprimido.
    win (lista) (int) (opc): Recebe as posições de vitória.
    velha (bool): Recebe deu velha.

    Retorno: None
    """
    #As variáveis a seguir recebem o texto e alteram-no caso tenha uma vitôria. Altera a cor do texto e do background
    p1 = tabuleiro[1] if 1 not in win else "\u001b[30;42m" + tabuleiro[1] + "\u001b[0m"
    p2 = tabuleiro[2] if 2 not in win else "\u001b[30;42m" + tabuleiro[2] + "\u001b[0m"
    p3 = tabuleiro[3] if 3 not in win else "\u001b[30;42m" + tabuleiro[3] + "\u001b[0m"
    p4 = tabuleiro[4] if 4 not in win else "\u001b[30;42m" + tabuleiro[4] + "\u001b[0m"
    p5 = tabuleiro[5] if 5 not in win else "\u001b[30;42m" + tabuleiro[5] + "\u001b[0m"
    p6 = tabuleiro[6] if 6 not in win else "\u001b[30;42m" + tabuleiro[6] + "\u001b[0m"
    p7 = tabuleiro[7] if 7 not in win else "\u001b[30;42m" + tabuleiro[7] + "\u001b[0m"
    p8 = tabuleiro[8] if 8 not in win else "\u001b[30;42m" + tabuleiro[8] + "\u001b[0m"
    p9 = tabuleiro[9] if 9 not in win else "\u001b[30;42m" + tabuleiro[9] + "\u001b[0m"
    start = "\u001b[30;41m" if (velha) else "\u001b[0m" #Altera o background caso dê velha
    print(f"+{'-' * 37}+")

    print(f"|{' ' * 13}", end = "")
    print(f"{start} {p7} | {p8} | {p9} ", end = "\u001b[0m") #end faz com que sempre retorne pra cor original no final, para não mudar o background mais que o necessário.
    print(f"{' ' * 13}|")

    print(f"|{' ' * 13}", end = "")
    print(f"{start}---+---+---", end = "\u001b[0m")
    print(f"{' ' * 13}|")

    print(f"|{' ' * 13}", end = "")
    print(f"{start} {p4} | {p5} | {p6} ", end = "\u001b[0m")
    print(f"{' ' * 13}|")

    print(f"|{' ' * 13}", end = "")
    print(f"{start}---+---+---", end = "\u001b[0m")
    print(f"{' ' * 13}|")

    print(f"|{' ' * 13}", end = "")
    print(f"{start} {p1} | {p2} | {p3} ", end = "\u001b[0m")
    print(f"{' ' * 13}|")

    print(f"+{'-' * 37}+")

def ganhou(tabuleiro, simbolo):
    """
    Função responsável por verificar se alguém ganhou.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para ser verificado.
    simbolo (str): Recebe o simbolo para ser usado na verificação;

    Retorno:
    bool: Caso tenha ganhado = True; Caso não tenha ganhado = False.
    lista: Caso tenha ganhado retorna a posição, se não, retorna None.
    """
    #Verifica toda possíbilidade de vitôria, comparando essas ao símbolo recebido.
    if (tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == simbolo):
        return True, [1, 2, 3]
    elif (tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == simbolo):
        return True, [4, 5, 6]
    elif (tabuleiro[7] == tabuleiro[8] == tabuleiro[9] == simbolo):
        return True, [7, 8, 9]
    elif (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == simbolo):
        return True, [1, 4, 7]
    elif (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == simbolo):
        return True, [2, 5, 8]
    elif (tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == simbolo):
        return True, [3, 6, 9]
    elif (tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == simbolo):
        return True, [1, 5, 9]
    elif (tabuleiro[7] == tabuleiro[5] == tabuleiro[3] == simbolo):
        return True, [7, 5, 3]
    return False, None

def disp(tabuleiro, l = [], i = 1):
    """
    Função responsável por retornar a quantidade de espaços disponíveis. - Função
        de Recursão.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para ser verificado.
    l (lista) (int) (opc): Lista usada na recursão que recebe os espaços vazios.
    i (int) (opc): Variavel contadora da recursão.

    Retorno:
    l (lista) (int): Lista com os espaços vazios.
    """
    if len(tabuleiro) > i: #Passa por todos elementos do tabuleiro
        if (tabuleiro[i] == " "): #Se o elemento i estiver vazio esse é adicionado em uma lista que será retornada.
            return disp(tabuleiro, l + [i], i + 1)
        return disp(tabuleiro, l, i + 1)
    return l

def cDisp(tabuleiro, li, l = [], i = 0):
    """
    Função responsável por verificar, a partir de uma lista,
    quais espaços estão em branco. - Função de Recursão.
    Usada para saber se os cantos estão disponível.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para fazer as verificações.
    li (lista) (int): Recebe uma lista com posições para serem verificadas.
    l (lista) (opc): Lista usada na recursão para receber os espaços disponíveis.
    i (int) (opc): Variável contadora usada na recursão.

    Retorno:
    l (lista) (int): Lista com os espaços que ainda podem ser ocupados.
    """
    if len(li) > i: #Passa por todos elementos da lista recebida
        if (tabuleiro[li[i]] == " "): #Verifica se os canto[i] é igual a vazio, se sim, salva esse numa lista que será retornada.
            return cDisp(tabuleiro, li, l + [li[i]], i + 1)
        return cDisp(tabuleiro, li, l, i + 1)
    return l

def fSimb(tabuleiro, simbolo, l = [], i = 1):
    """
    Função responsável por verificar as posições ocupadas por um símbolo. - Função
        de Recursão.

    Parametros:
    tabuleiro (lista) (str): Recebe o tabuleiro para fazer as verificações.
    simbolo (str): Recebe o símbolo para ser verificado.
    l (lista) (opc): Lista usada na recursão para receber os espaços ocupados por esse.
    i (int) (opc): Variável contadora usada na recursão.

    Retorno:
    l (lista) (opc): Lista com os valores ocupados pelo símbolo.
    """
    if (len(tabuleiro) > i): #Passa por toda o tabuleiro
        if (tabuleiro[i] == simbolo): #Se o tabuleiro na posição i for igual ao simbolo, essa é salva em uma lista que será retornada.
            return fSimb(tabuleiro, simbolo, l + [i], i + 1)
        return fSimb(tabuleiro, simbolo, l, i + 1)
    return l

def empate(tabuleiro):
    """
    Função responsável por verificar se há um empate.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para ser verificado.

    Retorno:
    boolean : Caso esteja empatado = True; Caso não esteja empatado = False.
    """
    return len([s for s in tabuleiro if (s == " ")]) == 0 #Se não tiver espaço em branco = empate

def recEStrat(lSimb, L = [], i = 0, j = 0):
    """
    Função responsavel por verificar, a partir de uma lista,
    quais movimentos são possíveis usando as condições de vitória. - Função
        de Recursão.

    Parâmetros:
    lSimb (lista) (int): Posições que vão ser verificadas para saber quais
        condições de vitória poderiam ocorrer.
    L (lista) (lista) (int) (opc): Lista usada na recursão com as posições que
        podem gerar uma vitória.
    i (int) (opc): Variável contadora de recursão responsável por iterar por
        todos elementos de lSimb.
    j (int) (opc): Variável contadora de recursão responsável por iterar por
        todos elementos de pos.

    Retorno:
    L (lista) (lista) (int): Valores que podem gerar uma vitória.
    """
    pos = [[1, 2, 3], [5, 4, 6], [7, 8, 9], [1, 4, 7], [5, 2, 8], [3, 6, 9], [5, 1, 9], [5, 7, 3]] #Posições de vitória, como mostado no primeiro exemplo do PDF.
    if len(lSimb) > i: #Usado para ter acesso as listas dentro da lista.
        if len(pos) > j: #Usado para ter acesso aos itens dentro das listas dentro da lista.
            if lSimb[i] in pos[j]: #Verifica se a posição que eu recebo de fSim está em alguma dessas possíbilidades.
                return recEStrat(lSimb, L + [pos[j]], i, j + 1)
            return recEStrat(lSimb, L, i, j + 1)
        return recEStrat(lSimb, L, i + 1, 0) #Retorna j para 0 para pular para a próxima lista
    return L

def rec(tabuleiro, poss, simboloComputador, empty = [], i = 0):
    """
    Função responsável por verificar, baseando-se em uma lista,
    se uma estratégia pode ser executada. Caso possa, seleciona também
    um movimento para ser executado. - Função de Recursão.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para ser usado em verificações.
    poss (lista) (int): Recebe uma lista com posições de tabuleiro para serem
        verificadas.
    simboloComputador (str): Recebe o símbolo do computador.
    empty (lista) (lista) (int) (opc): Caso esteja presente, recebe uma lista
        contendo as posições que devem estar vazias ou conter o símbolo do
        compudador para que a jogada possa ser executada.
    i (int): Variável contadora de recursão.

    Retorno:
    int: Posição escolhida, baseada na estratégia, para o computador marcar.
    None: Caso nenhuma posição da estratégia esteja disponível.
    """
    ok = False #Variável flag
    comp = lambda x: (x == " " or x == simboloComputador)
    #^ Função que confere se o valor recebido é igual ao simbolo do computador
    #ou se está disponível.
    if (len(poss) > i):
        #Testes para saber se os espaços em branco, para uma jogada dar certo, estão disponíveis.
        if (poss[i][0] == 5 and len(empty) != 0): #Casos em que se tem que ter mais atenção e verificar se fazem sentido (2º exemplo na parte de Estratégias)
            ok = comp(tabuleiro[empty[i][0]]) and (comp(tabuleiro[empty[i][1][0]]) or comp(tabuleiro[empty[i][1][0]]))
        elif (len(empty) != 0): #Se não, testam esses. (1º caso na parte de Estratégias)
            ok = comp(tabuleiro[empty[i][0]]) and comp(tabuleiro[empty[i][1]])
        else: #Caso a lista não seja passada e desejarmos usar no modo simples.
            ok = True

        if (comp(tabuleiro[poss[i][0]]) and comp(tabuleiro[poss[i][1]]) and comp(tabuleiro[poss[i][2]]) and ok): #Se todos forem iguais ao símbolo do Computador ou vazio. Caso tenhamos passado a lista, verificará também se passou nos testes anteriores.
            return poss[i][0] if (tabuleiro[poss[i][0]] == " ") else poss[i][1] if (tabuleiro[poss[i][1]] == " ") else poss[i][2] if (tabuleiro[poss[i][2]] == " ") else rec(tabuleiro, poss, simboloComputador, empty, i+1)
        return rec(tabuleiro, poss, simboloComputador, empty, i+1)
    return

def pVencer(tabuleiro, simbolo, i = 0):
    """
    Função responsável por dizer se um símbolo está proximo de vencer.
    Utilizada tanto para defesa quanto para o ataque.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para ser avaliado com base
        no símbolo.
    simbolo (str): Recebe o simbolo para avaliar o tabuleiro.
    i (int): Variável contadora de recursão.

    Retorno:
    int: Posição da vitória.
    none: Caso ainda não tenha uma posição de vitória.
    """
    pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]] #Posições de vitória, como mostado no primeiro exemplo do PDF.
    if (i < len(pos)):
        l2 = [tabuleiro[pos[i][0]]] + [tabuleiro[pos[i][1]]] + [tabuleiro[pos[i][2]]]
        if ((" " in l2) and (len([q for q in l2 if (q == simbolo)]) == 2)): #Se tiver 2 símbolos iguais ao recebido já marcados e tiver um espaço disponível pra completar a jogada
            return pos[i][0] if l2[0] == " " else pos[i][1] if l2[1] == " " else pos[i][2] #Retorna a posição baseado em qual está vazio.
        return pVencer(tabuleiro, simbolo, i + 1)
    return None

def indexR(l, simbolo, i = 0):
    """
    Função responsável por fazer o index - retornar a posição de um item.

    Parâmetros:
    l (lista): Lista de onde será tirado o index.
    simbolo: Item do qual faremos o index.
    i (int): Variável contadora de recursão.

    Retorno:
    Int: Posição onde encontramos o primeiro item igual a simbolo.
    None: Caso não encontre o index desse.
    """
    if len(l) > i:
        return i if(l[i] == simbolo) else indexR(l, simbolo, i + 1)
    return None

def eStrat(tabuleiro, simboloJogador, simboloComputador):
    """
    Função responsável pela resposta à algumas estrategias do jogador.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para avaliar as posições desse.
    simboloJogador (str): Recebe o simbolo do Jogador.
    simboloComputador (str): Recebe o simbolo do Computador.

    Retorno:
    None: Caso nenhuma estratégia tenha sido encontrada pelas condicionais.
    int: Caso alguma estratégia tenha sido encontrada e precisse ser impedida
        por essa função.
    """
    corners = [1, 7, 9, 3] #Cantos
    apoio = [2, 4, 6, 8] #Meios das extremidades
    fCorners = [[4, 2], [4, 8], [8, 6], [2, 6]] #Meios das extremidades adjacentes aos cantos
    fCornersOP = [6, 4] #Meios das extremidades opostos aos cantos
    fCornersOP2 = [2, 8] #Meios das extremidades opostos aos cantos
    l2 = [tabuleiro[corners[0]]] + [tabuleiro[corners[1]]] + [tabuleiro[corners[2]]] + [tabuleiro[corners[3]]] #Lista com todos os simbolos dos cantos
    l3 = [tabuleiro[2]] + [tabuleiro[4]] + [tabuleiro[6]] + [tabuleiro[8]] #Lista com todos os simbolos dos meios das extremidades
    qCorn = [i for i in l2 if (i == simboloJogador)] #Compreensão de lista para me dar os cantos que o jogador possui
    if (simboloJogador in l2): #Caso o jogador queira ganhar usando a estratégia de 2-3 cantos
        lSimb = fSimb(tabuleiro, simboloComputador)
        if (5 in lSimb and len(qCorn) == 2):
            r = 4 if (tabuleiro[4] == " ") else 6 if (tabuleiro[6] == " ") else None #Posição absoluta, 4 ou 3.
            if (r != None):
                return r
    if (simboloJogador in l2 and simboloJogador in l3 and len(qCorn) == 1 and len(disp(tabuleiro)) == 6): #Caso de duas vitórias (Olhar PDF, Caso "2º")
        gC = indexR(l2, simboloJogador)
        gIC = indexR(l3, simboloJogador)
        p1 = corners[gC]
        p2 = apoio[gIC]
        if (p1 == 7 and p2 == 2): #Faz todos por posição absoluta, baseado no que tem disponível e no que pode parar essas jogadas
            return 1 if 1 in disp(tabuleiro) else 4 if 4 in disp(tabuleiro) else 3 if 3 in disp(tabuleiro) else None
        elif (p1 == 9 and p2 == 2):
            return 3 if 3 in disp(tabuleiro) else 6 if 6 in disp(tabuleiro) else 1 if 1 in disp(tabuleiro) else None
        elif (p1 == 1 and p2 == 8):
            return 7 if 7 in disp(tabuleiro) else 4 if 4 in disp(tabuleiro) else 9 if 9 in disp(tabuleiro) else None
        elif (p1 == 3 and p2 == 8):
            return 9 if 9 in disp(tabuleiro) else 6 if 6 in disp(tabuleiro) else 7 if 7 in disp(tabuleiro) else None
    eDisp = disp(tabuleiro) #Espaços disponíveis
    fCorn = [i for i in l3 if (i == simboloJogador)] #Compreensão de lista para me dar os meios das extremidades que o jogador possui
    if (len(eDisp) == 7 and len(fCorn) > 0): #Caso dos meios das extremidades
        mCorn = [i for i in l2 if (i == simboloComputador)] #Compreensão de lista para me dar os cantos que o computador possui
        if len(mCorn) > 0: #Verifica se o computador tem um canto
            if (simboloComputador == tabuleiro[corners[0]]):
                lpC = fCorners[0]
                c = corners[0]
            elif (simboloComputador == tabuleiro[corners[1]]):
                lpC = fCorners[1]
                c = corners[1]
            elif (simboloComputador == tabuleiro[corners[2]]):
                lpC = fCorners[2]
                c = corners[2]
            elif (simboloComputador == tabuleiro[corners[3]]):
                lpC = fCorners[3]
                c = corners[3]

            posC = apoio[indexR(l3, simboloJogador)]

            if posC in lpC: #Caso escolham o meio das extremidades adjacentes (ver lista fCorners)
                return lpC[1] if (fCorn[0] == tabuleiro[lpC[0]]) else lpC[0]
            else:
                if posC in fCornersOP: #Caso escolham o meio das extreminades inverso (4, 6)
                    return 1 if (c == 7) else 7 if (c == 1) else 9 if (c == 3) else 3
                elif posC in fCornersOP2: #Caso escolham o meio das extremidades inverso (2, 8)
                    return 9 if (c == 7) else 3 if (c == 1) else 1 if (c == 3) else 7
        return None
    return None

def defesa(tabuleiro, simboloJogador, simboloComputador):
    """
    Função responsável por reunir todas as funções relativas à defesa.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para passa-lo para
        suas funções.
    simboloJogador (str): Recebe o simbolo do Jogador para passa-lo
        para suas funções.
    simboloComputador (str): Recebe o simbolo do Computador para passa-lo
        para suas funções.

    Retorno: (int ou None)
    vencer (int): Caso o jogador estiver prestes a ganhar.
    estrat (int): Caso o jogador estiver tentando executar alguma estratégia.
    None: Caso nenhuma estratégia do jogador tenha sido encontrada ou não esteja
        perto de vencer.
    """
    vencer = pVencer(tabuleiro, simboloJogador) #Verifica se vai vencer
    estrat = eStrat(tabuleiro, simboloJogador, simboloComputador) #Verifica se está tentando alguma estratégia
    return vencer if (vencer != None) else estrat

def strat(tabuleiro, simboloComputador):
    """
    Função responsável por reunir todas as funções relativas ao ataque.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro para passa-lo para suas funções.
    simboloComputador (str): Recebe o símbolo do computador para passa-lo para
        suas funções.

    Retorno: (int ou None)
    dispR (int): Caso alguma estratégia possa ser executada.
    nPos (int): Caso nenhuma estraégia possa ser executada e tenha uma chance de vitória.
    int: Posição aleatoria usando os espaços diponíveis caso não tenha uma chance de vitória.
    """
    strats = [[1, 9, 3], [1, 9, 7], [3, 7, 9], [1, 7, 3], [5, 7, 9], [5, 7, 1], [5, 9, 3], [5, 1, 3]]
    empty = [[2, 6], [4, 8], [6, 8], [4, 2], [8, [1, 3]], [4, [3, 9]], [6, [1, 7]], [2, [7, 9]]]
    #strats -> Contém as estratégias e empty -> Contém os espaços que precisam estar vazios pra poder ter as estratégias

    dispR = rec(tabuleiro, strats, simboloComputador, empty)
    if (dispR != None): #Se uma estratégia puder ser executada
        return dispR
    else:
        poss = recEStrat(fSimb(tabuleiro, simboloComputador)) #Cria uma lista com todas as chances de ganhar
        nPos = rec(tabuleiro, poss, simboloComputador) #Avalia baseado em todas as chances de ganhar
        return nPos if (nPos != None) else random.choice(disp(tabuleiro)) #Se não houver chance de ganhar, aleatorizamos uma posição.

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

    Estratégia: (Mais explicações no PDF)
    Verifica primeiro alguns casos padrões, caso não possam ser executados, passa a executar a estratégia.
        1ª parte: Tenta ver se é possível vencer com apenas uma jogada. Se não, vai para o segundo passo;
        2ª parte: Confere se precisa se defender, caso positivo se defenderá. Se não, vai para o terceiro passo;
        3º parte: Confere se é possível executar uma das estratégias e, caso não possa retornará um número que
            possa garantir um passo a mais para uma possível vitória ou um número aleatorio.
    """
    simboloJogador = "X" if (simboloComputador == "O") else "O" #Define o símbolo do jogador
    corners = [1, 7, 9, 3] #Cantos

    if ((len(disp(tabuleiro)) == 9)): #Jogada padrão nos cantos caso seja a primeira jogada
        return random.choice(cDisp(tabuleiro, corners)) #Aleatoriza um dos cantos
    elif ((len(disp(tabuleiro)) == 8) and (tabuleiro[5] == " ")): #Caso seja a segunda jogada e o 5 esteja vazio
        return 5 #Marca 5
    else:
        vencer = pVencer(tabuleiro, simboloComputador) #Tenta vencer se possível
        aDefesa = defesa(tabuleiro, simboloJogador, simboloComputador) #Tenta defender se necessário
        estrat = strat(tabuleiro, simboloComputador) #Se não, tenta alguma estrategia
        return vencer if (vencer != None) else aDefesa if (aDefesa != None) else estrat

def programa(tabuleiro, simboloJogador, simboloComputador, turno, count = 0):
    """
    Função responsável pela execução do programa, verificar se há vitória ou empate
        e quem deve jogar.

    Parâmetros:
    tabuleiro (lista) (str): Recebe o tabuleiro e passa esse para suas funções.
    simboloJogador (str): Recebe o símbolo do jogador para passa-lo para suas
        funções e verificar de quem é o turno.
    simboloComputador (str): Recebe o símbolo do computador para passa-lo para
        suas funções e verificar de quem é o turno.
    turno (str): Variável que alterna entre os símbolos de jogador e computador
        para saber de quem é o turno.
    count (int): Variável contadora de recursão para saber quantas jogadas válidas
        foram feitas.

    Retorno: None
    """
    if count >= 5:
        j, wPos1 = ganhou(tabuleiro, simboloJogador) #Verifica se o jogador ganhou
        pc, wPos2 = ganhou(tabuleiro, simboloComputador) #Verifica se o computador ganhou
        velha = empate(tabuleiro) #Verifica se deu velha

        if (j or pc or velha):
            txt = f"|{' ' * 9}O computador ganhou!{' ' * 8}|" if (pc) else f"|{' ' * 10}O jogador ganhou!{' ' * 10}|" if (j) else f"|{' ' * 14}Deu velha!{' ' * 13}|"
            limpaTela()
            pTab(tabuleiro, velha = True) if (not (j or pc)) else pTab(tabuleiro, wPos1) if j else pTab(tabuleiro, wPos2)
            #IFs para verificar se é velha, caso seja manda pro tabuleiro como velha, se não:
            #Caso tenha j tenha vencido manda wPos1, se não wPos2.
            print(f"+{'-' * 37}+")
            print(txt)
            print(f"+{'-' * 37}+")
            return

    if turno == simboloJogador: #Se for o turno do jogador
        pos = getPos(int, "Qual posição deseja marcar (1-9): ", ["Valor inválido.", "Você deve digitar", "um número inteiro entre 1 e 9."])
        if pos not in disp(tabuleiro): #Se a posição não estiver nos disponíveis
            print("Posição já preenchida. Tente novamente!")
            programa(tabuleiro, simboloJogador, simboloComputador, turno, count) #Continua no mesmo turno
        else: #Se a posição estiver disponíveis
            tabuleiro[pos] = simboloJogador
            programa(tabuleiro, simboloJogador, simboloComputador, simboloComputador, count + 1) #Vai pro turno do computador
    else: #Se for o turno do computador
        tabuleiro[jogadaComputador(tabuleiro, simboloComputador)] = simboloComputador #Faz a jogada do computador
        pTab(tabuleiro) #Imprime o tabuleiro
        programa(tabuleiro, simboloJogador, simboloComputador, simboloJogador, count + 1) #Muda o turno

def main():
    limpaTela()
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())
    #print(getMatricula())

    print(f"+{'-' * 37}+")
    print("| Seja bem-vindo(a) ao jogo da velha! |")
    print(f"+{'-' * 37}+")

    tabuleiro = [None, " ", " ", " ", " ", " ", " ", " ", " ", " "]
    simboloJogador, simboloComputador = xOuO();
    turno = first(simboloComputador)

    if turno != simboloComputador: #Se o primiero turno não for o do computador, imprime o tabuleiro vazio
        pTab(tabuleiro)

    programa(tabuleiro[:], simboloJogador, simboloComputador, turno)

################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()

#strats = [[1, 9, 3], [1, 9, 7], [7, 5, 9], [7, 5, 1], [9, 5, 3], [1, 5, 3], [3, 7, 9], [1, 7, 3]]