from os import system, name
#conferir documentação de todos
def limpa():
    """
    Função para limpar a tela.

    Parametros: Nenhum

    Returno: None
    """

    system('cls') if (name == 'nt') else system('clear')

    return

def Rinput(func, maxV = None, msg = "", msgE = ""):
    """
    Função responsavel por todos os inputs do EP.

    Tenta converter um dado input e, caso esse gere uma exceção, repete-se, 
    mostrando também uma mensagem de erro, até receber um valor valido.

    Parametros:
    func (função): Recebe a função que será usada para converter o input.
    maxV (int)(opc): Recebe o valor máximo que essa variavel pode ser.
    msg (str)(opc): Recebe a mensagem que será exposta no input.
    msgE (str)(opc): Recebe a mensagem de erro que será exposta caso haja 
    uma excessão ou, se estiver utilizando maxV, quando o número recebido
    no input seja menor que 1 ou maior que maxV.  

    Return:
    int -> Caso a func tenha recebido int como paramentro.
    float -> Caso a func tenha recebido float como parametro. 
    """
    try: 
        r = func(input(msg))
    except:
        print(msgE)
        return Rinput(func, maxV, msg, msgE)
    
    if ((maxV != None) and (1 <= r <= maxV)):
        return r
    elif (maxV != None):
        print(msgE)
        return Rinput(func, maxV, msg, msgE)
    
    return r

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
    elif (n == 6):
        return "Achocolatado", 12, 0, 0, 280, 0, 20, 2
    elif (n == 0):
        return "Água", 0, 0, 300, 0, 0, 0, 2
    
    return None, None, None, None, None, None, None, None

def fNota(n): #falta documentar
    x, y = 1, None

    n1 = 100
    
    if (n <= 11):
        if (n == 11):
            return 100, 1
        elif (1 < n < 6):
            n1 = 20
            n -= 2
        elif (6 < n < 9):
            x = 100
            n -= 6
        elif (n >= 9):
            x = 100
            n1 = 10
            n -= 9
            
        y = n1//2**n

    return (x, y) if (y != None) else (None, None)

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

    return (c >= 0 and a >= 0 and m >= 0 and cc >= 0), special(g), special(l), special(lv)

def menu(c, a, g, l, lv, m, cc, off = 0, i = 1, id1 = None, id2 = None, id3 = None, id4 = None, id5 = None, cnt = 0):
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
    off (int)(opc): Indica em qual menu estar.

    Returno: Int ou None.
    Int -> Indica o ID.
    None -> Indica que a opção não está presente.
    """
    Q_GELO = 5
    flag = False

    vf = lambda x, y, z = None: (y - x if (z == None) else z - y) if (x) else None
    uVar = lambda var, u, t = True, i = -1: u if ((var == None) and (t) and ((i != None) and (u != i))) else var

    ic = i + off

    nB, v, cB, aB, leB, mB, ccB, gelada = fDict(ic)

    if ((nB != None) and (cnt < 5)):
        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB) #talvez eu possa botar isso na def check

        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))):
            cnt += 1
            print(f"{cnt} - {nB} - {v} {'-' if (uG or uLV or uL) else ''} {'(G)' if (uG) else ''}{'(V)' if (uLV) else ''}{'(L)' if (uL) else ''}")
            flag = True
        
        return menu(c, a, g, l, lv, m, cc, off, i + 1, uVar(id1, ic, flag), uVar(id2, ic, flag, id1), uVar(id3, ic, flag, id2), uVar(id4, ic, flag, id3), uVar(id5, ic, flag, id4), cnt) #se decidir por não retornar nada remover e mudar um pouco a logica
    elif (cnt < 5):
        nB, v, cB, aB, leB, mB, ccB, gelada = fDict(0) #provavelmente pode ser transformado em função

        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB) #
        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))):#
            cnt += 1 
            print(f"{cnt} - {nB} - {v} {'-' if (uG or uLV or uL) else ''} {'(G)' if (uG) else ''}{'(V)' if (uLV) else ''}{'(L)' if (uL) else ''}")# responder c true/false pra poder fazer o resto da lógica de menu
            id1, id2, id3, id4, id5 = uVar(id1, 0), uVar(id2, 0, i = id1), uVar(id3, 0, i = id2), uVar(id4, 0, i = id3), uVar(id5, 0, i = id4)

    return id1, id2, id3, id4, id5

def troco(vT, i = 0, mult = None, m = None): #falta documentar
    rs = lambda m, mult: (f'0,{m}' if (m >= 10) else f'0,0{m}') if(mult == 100) else (f'{m},00')

    if (m != None):
        nm = m * (100/mult)
        if ((vT//nm) != 0):
            print(f"R$ {rs(m, mult)}")
            troco(vT - nm, i, mult, m)
        else:
            troco(vT, i + 1, None, None)
    else:
        vT = (vT * 100) if (i == 0) else vT
        r, r1 = fNota(i)
        troco(vT, i, r, r1) if (r != None) else None
    
    return

def programa(cup, c, a, g, l, lv, m, cc, off = 0): #falta documentar
    lch = lambda vl, v1, v2, v3, v4, v5: (v1 != vl and v2 != vl and v3 != vl and v4 != vl and v5 != vl)

    next = 0

    print("Produtos:")

    if cup > 0:
        id1, id2, id3, id4, id5 = menu(c, a, g, l, lv, m, cc, off)

        if (id1 == id2 == id3 == id4 == id5 == None):
            print("Aguardando Manutenção:\nFalta geral de ingredientes!")
        else:
            next = 5 if (id5 != None) else 4 if (id4 != None) else 3 if (id3 != None) else 2 if (id2 != None) else 1 if (id1 != None) else 0

            if (lch(0, id1, id2, id3, id4, id5) and lch(None, id1, id2, id3, id4, id5)): #none and 0
                off = id5
                next += 1
                print (f"{next} - Mostrar Mais")  

    else:
        print("Aguardando Manutenção:\nFalta de copo!")

    print("Outras:")
    print(f"{next + 1} - Informações dos Produtos")
    print(f"{next + 2} - Informações Internas")
    print(f"{next + 3} - Finalizar")

    q1 = Rinput(int, next + 3, "Digite a opção que deseja: ", f"Por favor, utilize números inteiros de 1-{next+3}.")

    if (q1 == next == 6):
        print("Proxima página") #incompleto
    elif (q1 == (next + 1)):
        print("Informações dos Produtos") #incompleto
    elif (q1 == (next + 2)):
        print("Informações Internas") #incompleto
    elif (q1 == (next + 3)):
        print("Finalizar") #incompleto
    else:
        if (q1 == 1):
            print("1ª opc") #incompleto
        elif (q1 == 2):
            print("2ª opc") #incompleto
        elif (q1 == 3):
            print("3ª opc") #incompleto
        elif (q1 == 4):
            print("4ª opc") #incompleto
        elif (q1 == 5):
            print("5ª opc") #incompleto
    
    _ = input("enter")
    return

def main():
    limpa()
    programa(10, 50, 500, 10, 500, 500, 70, 100) #(10, 50, 500, 10, 500, 500, 70, 100)
    #troco(94000) #limite maximo que eu iria com tranquilidade

main()

#problema de arredondamento + 0.0000001