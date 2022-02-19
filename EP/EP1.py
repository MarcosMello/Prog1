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

def Rinput(func, maxV = None, msg = "", msgE = "", minV = 1, flag = False):
    """
    Função responsavel por todos os inputs do EP.

    Tenta converter um dado input e, caso esse gere uma exceção, repete-se, 
    mostrando também uma mensagem de erro, até receber um valor valido.

    Parametros:
    func (função): Recebe a função que será usada para converter o input.
    maxV (float/int)(opc): Recebe o valor máximo que essa variavel pode ser.
    msg (str)(opc): Recebe a mensagem que será exposta no input.
    msgE (str)(opc): Recebe a mensagem de erro que será exposta caso haja 
    uma excessão ou, se estiver utilizando maxV, quando o número recebido
    no input seja menor que 1 ou maior que maxV.
    minV (float/int)(opc): Recebe o valor mínimo que essa variável pode ser.  

    Return:
    int -> Caso a func tenha recebido int como paramentro.
    float -> Caso a func tenha recebido float como parametro. 
    """
    try: 
        r = func(input(msg))
    except:
        print(msgE)
        return Rinput(func, maxV, msg, msgE, flag)

    minV, r, maxV, flag = ((minV * 100), (r * 100), (maxV * 100), True) if (minV < 0) else (minV, r, maxV, flag) 

    if ((maxV != None) and (minV <= r <= maxV)):
        return r if (not flag) else r/100
    elif (maxV != None):
        print(msgE)
        return Rinput(func, maxV, msg, msgE, flag)
    
    return r if (not flag) else r/100

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

def menu(c, a, g, l, lv, m, cc, Q_GELO, off = 0, i = 1, id1 = None, id2 = None, id3 = None, id4 = None, id5 = None, cnt = 0):
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
        
        return menu(c, a, g, l, lv, m, cc, Q_GELO, off, i + 1, uVar(id1, ic, flag), uVar(id2, ic, flag, id1), uVar(id3, ic, flag, id2), uVar(id4, ic, flag, id3), uVar(id5, ic, flag, id4), cnt)
    elif (cnt < 5):
        nB, v, cB, aB, leB, mB, ccB, gelada = fDict(0) #provavelmente pode ser transformado em função

        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB) #
        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))):#
            cnt += 1 
            print(f"{cnt} - {nB} - {v} {'-' if (uG or uLV or uL) else ''} {'(G)' if (uG) else ''}{'(V)' if (uLV) else ''}{'(L)' if (uL) else ''}")
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

def infoP(i = 0): #falta documentar
    p = lambda msg, val: print(msg) if (val > 0) else None

    nB, v, cB, aB, leB, mB, ccB, gelada = fDict(i)

    if (nB != None):
        print(f"\n{nB}: R${v} ", end = "")
        print("- (G)") if (gelada == 1) else print("- (Q)") if (gelada == 0) else print("- (G)(Q)")
        p(f"- {cB}g de café solúvel", cB)
        p(f"- {aB}ml de água", aB)
        p(f"- {leB}ml de leite", leB)
        p(f"- {mB}g de preparado para Chá-mate", mB)
        p(f"- {ccB}ml de calda de chocolate", ccB)

        infoP(i+1)
    else:
        _ = input("\nPressione ENTER(<-') para retornar para o menu...")
    
    return

def infoI(cup, c, a, g, l, lv, m, cc, fat, fim = False):

    print("Informações Internas:\n")

    print(f"Copos: {cup}")
    print(f"Água: {a}")
    print(f"Café Solúvel: {c}")
    print(f"Gelo: {g}")
    print(f"Leite Comum: {l}")
    print(f"Leite Vegetal: {lv}")
    print(f"Preparado para Chá-mate: {m}")
    print(f"Calda de Chocolate: {cc}")
    print(f"Faturamento: R${fat}")

    _ = input(f"\nPressione ENTER(<-') para {'retornar para o menu...' if (not fim) else 'finalizar...'}") 

    return

def venda(c, a, g, l, lv, m, cc, Q_GELO, id): #falta documentar
    fL = lambda op1, op2, id: op1 if (id != 0) else op2

    nB, v, cB, aB, leB, mB, ccB, gelada = fDict(id)

    print(f"Você escolheu {fL('o', 'a', id)} {nB}")
    print(f"Preço: R${v}")

    if ((gelada > 1) and (g - Q_GELO >= 0)):
        txt = f"Deseja que {fL('seu', 'sua', id)} {nB} seja preparad{fL('o', 'a', id)} {fL('Quente', 'Tmp. Natural', id)} (1) ou Gelad{fL('o', 'a', id)} (2)? "
        rsp = Rinput(int, 2, txt, "Por favor, utilize apenas os números 1 e 2.")
        g -= Q_GELO if (rsp == 2) else 0
    elif (gelada == 1):
        g -= Q_GELO
    
    if((leB > 0) and ((l - leB) >= 0) and ((lv - leB)  >= 0)):
        txt = f"Deseja que seu {nB} seja preparado com Leite Comum (1) ou Leite Vegetal (2)? "
        rsp = Rinput(int, 2, txt, "Por favor, utilize apenas os números 1 e 2.")
        l, lv = ((l - leB), lv) if (rsp == 1) else (l, (lv-leB))
    elif((leB > 0) and ((l - leB) >= 0)):
        l -= leB
    elif((leB > 0) and ((lv - leB) >= 0)):
        lv -= leB
    
    return (c - cB), (a - aB), g, l, lv, (m - mB), (cc - ccB), v

def pix(v):
    rsp = Rinput(float, 94000.00, "Insira o dinheiro: ", "Por favor, utilize apenas os números entre 0.01 e 94000.", 0.01)
    
    dif = round(rsp - v, 2)

    if (dif >= 0):
        return dif

    return pix(round(v - rsp, 2))

def programa(cup, c, a, g, l, lv, m, cc, off = 0, fat = 0): #falta documentar
    Q_GELO = 5 #Quantidade de gelo necessaria para o preparo das bebidas geladas

    limpa()
    lch = lambda vl, v1, v2, v3, v4, v5: (v1 != vl and v2 != vl and v3 != vl and v4 != vl and v5 != vl)

    next = 0

    print("Produtos:")

    if cup > 0:
        id1, id2, id3, id4, id5 = menu(c, a, g, l, lv, m, cc, Q_GELO, off)

        if (id1 == id2 == id3 == id4 == id5 == None):
            print("Aguardando Manutenção:\nFalta geral de ingredientes!")
        else:
            next = 5 if (id5 != None) else 4 if (id4 != None) else 3 if (id3 != None) else 2 if (id2 != None) else 1 if (id1 != None) else 0

            if (lch(0, id1, id2, id3, id4, id5) and lch(None, id1, id2, id3, id4, id5)): #none and 0
                next += 1
                print (f"{next} - Mostrar Mais")  

    else:
        print("Aguardando Manutenção:\nFalta de copo!")

    print("Outras:")
    print(f"{next + 1} - Informações dos Produtos")
    print(f"{next + 2} - Informações Internas")
    print(f"{next + 3} - Finalizar\n")

    q1 = Rinput(int, next + 3, "Digite a opção que deseja: ", f"Por favor, utilize números inteiros de 1-{next+3}.")

    if (q1 == next == 6):
        off = id5
        programa(cup, c, a, g, l, lv, m, cc, off, fat)
    elif (q1 == (next + 1)):
        limpa()
        print("Produtos:")
        print("Legenda: (Q) -> Quente; (G) -> Gelada.")
        infoP()
    elif (q1 == (next + 2)):
        limpa()
        infoI(cup, c, a, g, l, lv, m, cc, fat)
    elif (q1 == (next + 3)):
        limpa()
        print("Finalizando!")
        infoI(cup, c, a, g, l, lv, m, cc, fat, True)
        exit()
    else:
        if (q1 == 1):
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id1)
        elif (q1 == 2):
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id2)
        elif (q1 == 3):
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id3)
        elif (q1 == 4):
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id4)
        elif (q1 == 5):
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id5)

        fat += v
        qtroco = pix(v)
        (print("Pegue seu troco: "), troco(qtroco)) if (qtroco > 0) else print("Troco: R$ 0.00")

        txt = f"Deseja comprar outro produto? (Sim (1); Não (2)) "
        rsp = Rinput(int, 2, txt, "Por favor, utilize apenas os números 1 e 2.")
        (limpa(), print("Finalizando!"), infoI(cup, c, a, g, l, lv, m, cc, fat, True), exit()) if (rsp == 2) else None

    programa(cup, c, a, g, l, lv, m, cc, off, fat)

    return

def main():
    programa(10, 50, 500, 10, 500, 500, 70, 100) #(10, 50, 500, 10, 500, 500, 70, 100)
    #troco(94000) #limite maximo que eu iria com tranquilidade

main()