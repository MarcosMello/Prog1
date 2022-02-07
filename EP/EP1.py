from os import system, name

def limpa():
    """
    Função para limpar a tela.

    Parametros: Nenhum

    Returno: None
    """

    system('cls') if (name == 'nt') else system('clear')

    return

def fDict(n):
    """
    Função que retorna todos valores necessários para construir o item. Nesta que
    devem ser adicionado os novos sabores.

    Parametros:
    n (int) = ID da bebida.

    Return:
    string: Nome da bebida.
    float: Valor da bebida.
    int: Quantidade de café soluvel necessário para o preparo.
    int: Quantidade de água necessária para o preparo.
    int: Quantidade de leite necessário para o preparo.
    int: Quantidade de preparado de mate necessário para o preparo.
    int: Quantidade de calda de chocolate necessária para o preparo.
    int: Indica se a bebida pode ser preparada gelada. 0 -> Para apenas quente,
         1 -> Para apenas gelada e 2 (ou outros) -> Para ambos. 
    None: Caso a bebida não exista.
    """

    if (n == 1):
        return "Expresso", 6, 50, 250, 0, 0, 0, 0
    elif (n == 2):
        return "Café Gelado", 8, 50, 300, 0, 0, 0, 1
    elif (n == 3):
        return "Chá Mate", 8, 0, 300, 0, 7, 0, 2
    elif (n == 4):
        return "Café com Leite", 9, 50, 200, 150, 0, 0, 2
    elif (n == 5):
        return "Macchiato de Chocolate", 14, 50, 250, 50, 0, 10, 2
    elif (n == 0):
        return "Água", 0, 0, 300, 0, 0, 0, 2
    
    return None, None, None, None, None, None, None, None

def check(c = 0, a = 0, g = None, l = None, lv = None, m = 0, cc = 0):
    """
    Função responsavel por verificar se o item pode ser adicionado no menu
    por meio da quantidade de itens disponíveis.

    Paramentos: Q. = Quantidade; (opc) = Parametro opcional.
    c (int)(opc): (Q. de café disponível - Q. de café necessario para o preparo).
    a (int)(opc): (Q. de água disponível - Q. de água necessario para o preparo).
    g (int)(opc): (Q. de gelo disponível - Q. de gelo necessario para o preparo).
    l (int)(opc): (Q. de leite disponível - Q. de leite necessario para o preparo).
    lv (int)(opc): (Q. de leite veg. disponível - Q. de leite veg. necessario para o preparo).
    m (int)(opc): (Q. de mate disponível - Q. de mate necessario para o preparo).
    cc (int)(opc): (Q. de calda choc. disponível - Q. de calda choc. necessario para o preparo).

    Retorno:
    bool: True, se os itens não especiais -Exceto gelo e leites- enviados forem >= 0 - Isso 
    indica que pode haver o preparo da bebida -, caso contrario, False.
    bool: True, se a bebida puder ser preparada gelada e tiver gelo suficiente, caso 
    contrario, False.
    bool: True, se a bebida puder ser preparada com leite e tiver Q. suficiente desse,
    caso contrario, False.
    bool: True, se a bebida puder ser preparada com leite veg. e tiver Q. suficiente 
    desse, caso contrario, False.  
    """
    special = lambda x: True if ((not x == None) and x >= 0) else False

    return c >= 0 and a >= 0 and m >= 0 and cc >= 0, special(g), special(l), special(lv)

def menu(c, a, g, l, lv, m, cc, i = 0):
    """
    Função responsável pelo menu, mantendo-os
    sempre atualizados com base na quatidade de ingredientes disponíveis.

    Parametros:
    c (int): Quantidade disponível de café solúvel em gramas (g).
    a (int): Quantidade disponível de água em mililitros (ml).
    g (int): Quantidade disponível de cubos de gelo (un).
    l (int): Quantidade disponível de leite em mililitros (ml).
    lv (int): Quantidade disponível de leite veg. em mililitros (ml).
    m (int): Quantidade disponível de mate em mililitros (g).
    cc (int): Quantidade disponível de calda de chocolate em mililitros (ml).

    Returno: None
    """
    #"Expresso", 6, 50, 250, 0, 0, 0, 0
    #nome, v, c, a, leites, m, cc, gelado?
    Q_GELO = 5

    vf = lambda x, y, z = None: (y - x if (z == None) else z - y) if (x) else None

    nB, v, cB, aB, leB, mB, ccB, gelada = fDict(i + 1)

    if nB != None:
        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB)

        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))):
            print(f"{i+1} - {nB} - {v} {'-' if (uG or uLV or uL) else ''} {'(G)' if (uG) else ''}{'(V)' if (uLV) else ''}{'(L)' if (uL) else ''}")
        
        return menu(c, a, g, l, lv, m, cc, i + 1) #se decidir por não retornar nada remover e mudar um pouco a logica
    else:
        nB, v, cB, aB, leB, mB, ccB, gelada = fDict(0) #provavelmente pode ser transformado em função

        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB) #

        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))):# 
            print(f"{i+1} - {nB} - {v} {'-' if (uG or uLV or uL) else ''} {'(G)' if (uG) else ''}{'(V)' if (uLV) else ''}{'(L)' if (uL) else ''}")# responder c true/false pra poder fazer o resto da lógica de menu

    return

def main():
    limpa()
    menu(50, 500, 10, 500, 500, 70, 100)

main()

#criar uma função recursiva para imprimir todas as entradas, nessa função fazer
#num += id * (10^n -variavel recursiva que começa com 0, para o primeiro ser = 1)
#retornar isso no final e depois ter uma logica para dar unpacking nisso (basicamente
#o exemplo de como separar o n e somar os digitos, só que sem a parte de somar
#a variavel que vai passar por todos os IDS começa com 1, e quando chegar em NONE, vai
#puxar a água que é o 0