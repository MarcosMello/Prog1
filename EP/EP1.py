from os import system, name

def limpa():
    """
    Função para limpar a tela.

    Parametros: Nenhum

    Retorno: None
    """

    system('cls') if (name == 'nt') else system('clear') #Função clear

    return

def Rinput(func, maxV = None, msg = "", msgE = "", minV = 1, flag = False):
    """
    Função responsável por todos os inputs do EP.

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
    flag (bool)(opc): Define se estamos lidando com numeros floats com valores após a virgula.  

    Retorno:
    int -> Caso a func tenha recebido int como paramentro.
    float -> Caso a func tenha recebido float como parametro. 
    """
    try: #Tenta converter
        r = func(input(msg))
    except: #Caso tenha erro durante conversão
        print(msgE)
        return Rinput(func, maxV, msg, msgE, flag) #Recursão até ter um valor possível

    minV, r, maxV, flag = ((minV * 100), (r * 100), (maxV * 100), True) if (minV < 0) else (minV, r, maxV, flag) 
    #^ Se nosso valor minimo for menor que 0, multiplicaremos os valores por 100 para evitar usar comparações entre floats

    if ((maxV != None) and (minV <= r <= maxV)): #Se tivermos um valor máximo e r estiver dentro dos limites:
        return (r) if (not flag) else (r/100) #Retorna r se for maior que 0, se não r/100 
    elif (maxV != None): #Se tivermos um valor máximo e r não estiver dentro dos limites:
        print(msgE)
        return Rinput(func, maxV, msg, msgE, flag) #Recursão até chegar em um valor válido
    
    return (r) if (not flag) else (r/100) #Retorna r se for maior que 0, se não r/100 

def fDict(n):
    """
    Função que retorna todos valores necessários para construir o item. Nesta que
    devem ser adicionado os novos sabores.

    Parametros:
    n (int): ID da bebida.

    Retorno:
    int: Quantidade de letras que o nome da bebida possui (Inclui espaços) * -1.
    string: Nome da bebida.
    float: Valor da bebida.
    int: Quantidade de café soluvel necessário para o preparo.
    int: Quantidade de água necessária para o preparo.
    int: Quantidade de leite necessário para o preparo.
    int: Quantidade de preparado de mate necessário para o preparo.
    int: Quantidade de calda de chocolate necessária para o preparo.
    int: Indica se a bebida pode ser preparada gelada. 0 -> Para apenas quente,
         1 -> Para apenas gelada e 2 (ou outros) -> Para ambos. 
    int, None, None, int, int, int, int, int, None: Indica a quantidade de letras 
        do nome da maior bebida e a menor quantidade necessário de cada ingrediente
        para o preparo das bebidas, caso a bebida não exista. 
    """

    if (n == 1):
        return -8, "Expresso", 6, 50, 250, 0, 0, 0, 0
    elif (n == 2):
        return -11, "Café Gelado", 8, 50, 300, 0, 0, 0, 1
    elif (n == 3):
        return -8, "Chá Mate", 8, 0, 300, 0, 7, 0, 2
    elif (n == 4):
        return -14, "Café com Leite", 9, 50, 200, 150, 0, 0, 2
    elif (n == 5):
        return -22, "Macchiato de Chocolate", 14, 50, 250, 50, 0, 10, 2
    elif (n == 6):
        return -12, "Achocolatado", 12, 0, 0, 280, 0, 20, 2
    elif (n == 0):
        return -12, "Água c/ Gelo", 3, 0, 300, 0, 0, 0, 1
    
    #Caso adicione alguma bebida com valores inferiores a esse é necessário mudar
    #Não utilizar nomes de bebidas com mais que 22 caracteres
    return -22, None, None, 50, 200, 50, 7, 10, None 

def fNota(n):
    """
    Função que retorna as notas/moedas em que o troco pode ser devolvido.
    Notas: 100, 50, 20, 10, 5, 2 -> 0, 1, 2, 3, 4, 5
    Moedas: 1, 0.50, 0.25, 0.10, 0.05, 0.01 -> 6, 7, 8, 9, 10, 11

    Paramentros:
    n (int): Indica qual nota/moeda vai ser retornada com base na ordem acima.

    Retorno:
    int: Indica se é nota (1) ou se é moeda (100).
    int: Valor da nota/moeda. 
    """
    x, y = 1, None

    n1 = 100
    
    if (n <= 11): #Caso n seja maior que 11, responderemos direto (None, None)
        if (n == 11):
            return 100, 1 #Retorna 1 centavo
        elif (1 < n < 6): #Faz o próximo número, após 50 ser 20 ao invés de 25. (Parte das Notas)
            n1 = 20
            n -= 2
        elif (6 < n < 9): #Faz o próximo número, após 2 começar de 100 ou 1 -uma vez que estamos falando de moedas nesse momento.
            x = 100
            n -= 6
        elif (n >= 9):  #Faz o próximo número, após 25 ser 10 ao invés de 12.5. (Parte das moedas)
            x = 100
            n1 = 10
            n -= 9
            
        y = n1//2**n #Equação para calcular as notas que não entrarem no caso fixo (11) acima.

    return (x, y) if (y != None) else (None, None) 

def check(c = 0, a = 0, g = None, l = None, lv = None, m = 0, cc = 0):
    """
    Função responsável por verificar se o item pode ser adicionado no menu
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
    special = lambda x: True if ((not x == None) and x >= 0) else False #Condição para os itens especiais, caso esses sejam diferentes de None e maiores ou iguais a zero, True, se não False.

    return (c >= 0 and a >= 0 and m >= 0 and cc >= 0), special(g), special(l), special(lv)

def menu(cup, c, a, g, l, lv, m, cc, Q_GELO, off = 0, i = 1, id1 = None, id2 = None, id3 = None, id4 = None, id5 = None, cnt = 0):
    """
    Função responsável pelo menu, mantendo-os
    sempre atualizados com base na quatidade de ingredientes disponíveis.

    Parametros:
    cup (int): Quantidade disponível de copos (un).
    c (int): Quantidade disponível de café solúvel em gramas (g).
    a (int): Quantidade disponível de água em mililitros (ml).
    g (int): Quantidade disponível de cubos de gelo (un).
    l (int): Quantidade disponível de leite em mililitros (ml).
    lv (int): Quantidade disponível de leite veg. em mililitros (ml).
    m (int): Quantidade disponível de mate em mililitros (g).
    cc (int): Quantidade disponível de calda de chocolate em mililitros (ml).
    Q_GELO (int): Quantidade de gelo necessária para o preparo das bebidas (un).
    off (int)(opc): Indica em qual menu estar (offset).
    i (int)(opc): Contador responsável por determinar o item de fDict() da iteração.
    id1 (int)(opc): Responsável por armazenar o ID da primeira bebida.
    id2 (int)(opc): Responsável por armazenar o ID da segunda bebida.
    id3 (int)(opc): Responsável por armazenar o ID da terceira bebida.
    id4 (int)(opc): Responsável por armazenar o ID da quarta bebida.
    id5 (int)(opc): Responsável por armazenar o ID da quinta bebida.
    cnt (int)(opc): Contador responsável por dar, aos itens, os números que são mostrados no menu.

    Retorno: Int ou None.
    Int -> Indica o ID.
    None -> Indica que a opção não está presente.
    """
    #Variáveis de cores
    WHITE = '\033[37m'
    BWHITE = '\033[97m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'

    SPACES = 34 - 1 #Espaços para a parte de 'Produtos e Variações*' do menu
    flag = False #Caso a bebida possa ser produzida.

    vf = lambda x, y, z = None: (y - x if (z == None) else z - y) if (x) else None #Caso x != 0, analizará z que se for != none responderá z-y, se não y-x. Isso é usado para mandar as diferenças para check.
    uVar = lambda var, u, t = True, i = -1: u if ((var == None) and (t) and ((i != None) and (u != i))) else var #Função que dá valor aos ids, verificando se esses já não estavam ocupados.

    ic = i + off #Possibilita a troca de páginas quando somado a um offset diferente de 0

    space, nB, v, cB, aB, leB, mB, ccB, gelada = fDict(ic) #Item de fDict

    if ((cup > 0) and (nB != None) and (cnt < 5)): #Caso a bebida exista e tenha mais que 0 copos e menos que 5 itens já setados.
        space += SPACES
        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB)

        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))): #Se a bebida puder ser produzida
            cnt += 1
            
            #Faz um item de 'Produtos e Variações*'
            space -= (3 if (uG) else 0) + (3 if(uLV) else 0) + (3 if(uL) else 0)
            print(f"|{' ' * 3}{cnt}{' ' * 3}|", end = "")
            print(f"{' ' * (space//2)}{nB} ", end = "")
            print(f"{f'{CYAN}(G){WHITE}' if (uG) else ''}{f'{GREEN}(V){WHITE}' if (uLV) else ''}{f'{BWHITE}(L){WHITE}' if (uL) else ''}", end = "")
            print(f"{' ' * (space//2 if (space%2 == 0) else space//2 + 1)}", end = "")
            valor = f"|  {GREEN}R$ {v:.2f}{WHITE}  |" if (v >= 10) else f"|  {GREEN}R$  {v:.2f}{WHITE}  |"
            print(valor)

            flag = True
        
        #v Chama a recursão para analizar todos os itens de fDict()
        return menu(cup, c, a, g, l, lv, m, cc, Q_GELO, off, i + 1, uVar(id1, ic, flag), uVar(id2, ic, flag, id1), uVar(id3, ic, flag, id2), uVar(id4, ic, flag, id3), uVar(id5, ic, flag, id4), cnt)
    elif ((cup > 0) and (cnt < 5)): #Caso a bebida não exista e tenha copo e tenha menos de 5 itens
        space, nB, v, cB, aB, leB, mB, ccB, gelada = fDict(0) #Água
        space += SPACES
        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB) 
        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))): #Se a bebida puder ser produzida
            cnt += 1

            #Faz um item de 'Produtos e Variações*'
            space -= (3 if (uG) else 0) + (3 if(uLV) else 0) + (3 if(uL) else 0) 
            print(f"|{' ' * 3}{cnt}{' ' * 3}|", end = "")
            print(f"{' ' * (space//2)}{nB} ", end = "")
            print(f"{f'{CYAN}(G){WHITE}' if (uG) else ''}{'{GREEN}(V){WHITE}' if (uLV) else ''}{'{BWHITE}(L){WHITE}' if (uL) else ''}", end = "")
            print(f"{' ' * (space//2 if (space%2 == 0) else space//2 + 1)}", end = "")
            valor = f"|  R$ {v:.2f}  |" if (v >= 10) else f"|  {GREEN}R$  {v:.2f}{WHITE}  |"
            print(valor)

            id1, id2, id3, id4, id5 = uVar(id1, 0), uVar(id2, 0, i = id1), uVar(id3, 0, i = id2), uVar(id4, 0, i = id3), uVar(id5, 0, i = id4) #Atualiza os valores das variáveis id1-5 sem chamar uma nova recursão.

    return id1, id2, id3, id4, id5

def troco(vT, i = 0, mult = None, m = None):
    """
    Função responsável por calcular e imprimir o troco.

    Parametros:
    vT (float): Valor do troco.
    i (int)(opc): Contador responsável por determinar o item de fNota() da iteração.
    mult (int)(opc): Variável que indica se é moeda (100) ou nota (1).
    m (int)(opc): Variável que contém a moeda/nota.

    Retorno: None
    """
    rs = lambda m, mult: (f'0,{m}' if (m >= 10) else f'0,0{m}') if(mult == 100) else (f'{m},00') #Formata a mensagem com base nos multiplicadores e se são maiores e iguais a 10 ou não.

    if (m != None): #Caso não m não esteja setado (início e caso a quantidade de notas iguais tenham acabado)
        nm = m * (100/mult)
        if ((vT//nm) != 0):
            print(f"R$ {rs(m, mult)}")
            troco(vT - nm, i, mult, m) #Recursão até acabar todas as notas iguais 
        else:
            troco(vT, i + 1, None, None) #Recursão para mudar o m e o mult
    else:
        vT = (vT * 100) if (i == 0) else vT #Multiplicando caso seja o início para que não use float
        r, r1 = fNota(i) #Recebe os novos m e mult
        troco(vT, i, r, r1) if (r != None) else None 
        #^ Se R não existir - caso já tenhamos avaliado todos as notas/moedas- devolve um none e deixa chegar ao return final. Caso exista, faz uma recursão com os novos m e mult.
    
    return

def countN(n): 
    """
    Função responsável por contar quantos dígitos um número -diferente de 0- possui.

    Parametros:
    n (float ou int): Número que vai ser contado.

    Retorno:
    int: Quantidade de dígitos.
    """
    if (n == 0):
        return 0 #Caso não tenhamos mais números para tirar casas
    
    return 1 + countN(n//10) #Adiciona 1 a recursão caso n não seja 0. (n//10) pois estamos tirando sempre uma casa decimal.

def infoP(Q_GELO, i = 0):
    """
    Função responsável por imprimir as informações dos produtos.

    Parametros:
    i (int)(opc): Variável responsável por determinar o item de fDict() da iteração. 

    Retorno: None
    """
    #Variáveis de cores
    WHITE = '\033[37m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    YELLOW = '\033[33m'

    SPACES = 55 #Espaços para contruir a tela

    p = lambda msg, val: print(msg) if (val > 0) else None #Só imprime a linha caso o valor do ingrediente seja maior que 0
    nN = lambda n, var: (n + countN(var)) if(var != 0) else (n + 1) #Chama countN() para contar quantos espaços tem que ser dados se var != 0

    space, nB, v, cB, aB, leB, mB, ccB, gelada = fDict(i) #Item de fDict
    space *= -1 #Convertendo espaço pra positivo 

    if (nB != None):
        qL1 = space + 8; #Tamanho do nome da bebida + quantidade de caracteres necessários para formar a linha
        
        #Tela de Informações de Produto
        print(f"+{'-' * SPACES}+") #Cabeçalho +--+

        print(f"|{' ' * fSpace(v, qL1, SPACES)}{PURPLE}{nB}{WHITE}: {GREEN}R$ {v:.2f}{WHITE}{' ' * fSpace(v, qL1, SPACES, True)}|")

        txt, qL = (f"Bebida {RED}Quente{WHITE}", 13) if (gelada == 0) else (f"Bebida {CYAN}Gelada{WHITE}", 13) if (gelada == 1) else (f"Bebida {RED}Quente{WHITE} ou {CYAN}Gelada{WHITE}", 23)
        print(f"|{' ' * fSpace(None, qL, SPACES)}{txt}{' ' * fSpace(None, qL, SPACES, True)}|")

        p(f"|{' ' * fSpace(None, nN(19, cB), SPACES)}- {cB}g de café solúvel{' ' * fSpace(None, nN(19, cB), SPACES, True)}|", cB)
        p(f"|{' ' * fSpace(None, nN(12, aB), SPACES)}- {aB}ml de água{' ' * fSpace(None, nN(12, aB), SPACES, True)}|", aB)
        p(f"|{' ' * fSpace(None, nN(22, Q_GELO), SPACES)}- {Q_GELO}un de pedras de gelo{' ' * fSpace(None, nN(22, Q_GELO), SPACES, True)}|", gelada)
        p(f"|{' ' * fSpace(None, nN(13, leB), SPACES)}- {leB}ml de leite{' ' * fSpace(None, nN(13, leB), SPACES, True)}|", leB)
        p(f"|{' ' * fSpace(None, nN(30, mB), SPACES)}- {mB}g de preparado para Chá-mate{' ' * fSpace(None, nN(30, mB), SPACES, True)}|", mB)
        p(f"|{' ' * fSpace(None, nN(26, ccB), SPACES)}- {ccB}ml de calda de chocolate{' ' * fSpace(None, nN(26, ccB), SPACES, True)}|", ccB)
        
        print(f"+{'-' * SPACES}+")

        infoP(Q_GELO, i+1) #Recursão para todos os itens de fDict() começando de Água c/ Gelo
    else:
        _ = input(f"\nPressione {YELLOW}ENTER(<-'){WHITE} para retornar para o menu...") #Input para segurar a tela antes de voltar para o menu
    
    return

def infoI(cup, c, a, g, l, lv, m, cc, fat, fim = False):
    """
    Função responsável por imprimir as informações internas.

    Parametros:
    cup (int): Quantidade disponível de copos (un).
    c (int): Quantidade disponível de café solúvel em gramas (g).
    a (int): Quantidade disponível de água em mililitros (ml).
    g (int): Quantidade disponível de cubos de gelo (un).
    l (int): Quantidade disponível de leite em mililitros (ml).
    lv (int): Quantidade disponível de leite veg. em mililitros (ml).
    m (int): Quantidade disponível de mate em mililitros (g).
    cc (int): Quantidade disponível de calda de chocolate em mililitros (ml).
    fat (int): Faturamento (R$).
    fim (int)(opc): Indica que estamos finalizando o programa.

    Retorno: None
    """
    #Variáveis de cores
    WHITE = '\033[37m'
    YELLOW = '\033[33m'

    SPACES = 55 #Espaços para contruir a tela

    nN = lambda n, var: (n + countN(var)) if(var != 0) else (n + 1) #Chama countN() para contar quantos espaços tem que ser dados se var != 0

    #Tela de Informações Internas
    print(f"+{'-' * SPACES}+") #Cabeçalho +--+
    print(f"|{' ' * fSpace(None, 21, SPACES)}Informações Internas:{' ' * fSpace(None, 21, SPACES, True)}|")
    print(f"+{'-' * SPACES}+")

    print(f"|{' ' * fSpace(None, nN(9, cup), SPACES)}- Copos: {cup}{' ' * fSpace(None, nN(9, cup), SPACES, True)}|")
    print(f"|{' ' * fSpace(None, nN(8, a), SPACES)}- Água: {a}{' ' * fSpace(None, nN(8, a), SPACES, True)}|")
    print(f"|{' ' * fSpace(None, nN(16, c), SPACES)}- Café Solúvel: {c}{' ' * fSpace(None, nN(16, c), SPACES, True)}|")
    print(f"|{' ' * fSpace(None, nN(8, g), SPACES)}- Gelo: {g}{' ' * fSpace(None, nN(8, g), SPACES, True)}|")
    print(f"|{' ' * fSpace(None, nN(15, l), SPACES)}- Leite Comum: {l}{' ' * fSpace(None, nN(15, l), SPACES, True)}|")
    print(f"|{' ' * fSpace(None, nN(17, lv), SPACES)}- Leite Vegetal: {lv}{' ' * fSpace(None, nN(17, lv), SPACES, True)}|")
    print(f"|{' ' * fSpace(None, nN(27, m), SPACES)}- Preparado para Chá-mate: {m}{' ' * fSpace(None, nN(27, m), SPACES, True)}|")
    print(f"|{' ' * fSpace(None, nN(22, cc), SPACES)}- Calda de Chocolate: {cc}{' ' * fSpace(None, nN(22, cc), SPACES, True)}|")
    print(f"|{' ' * fSpace(None, 21 + nN(0, fat), SPACES)}- Faturamento: R$ {fat:.2f}{' ' * fSpace(None, 21 + nN(0, fat), SPACES, True)}|")
    print(f"+{'-' * SPACES}+")

    _ = input(f"\nPressione {YELLOW}ENTER(<-'){WHITE} para {'retornar para o menu...' if (not fim) else 'finalizar...'}") #Input para segurar a tela antes de voltar para o menu ou finalizar

    return

def venda(c, a, g, l, lv, m, cc, Q_GELO, id):
    """
    Função responsável pelas coisas relativas à venda. 
    (Qual bebida está sendo vendida, se está sendo vendida quente ou gelada e 
    se está usando leite comum ou vegetal.)

    Parametros:
    c (int): Quantidade disponível de café solúvel em gramas (g).
    a (int): Quantidade disponível de água em mililitros (ml).
    g (int): Quantidade disponível de cubos de gelo (un).
    l (int): Quantidade disponível de leite em mililitros (ml).
    lv (int): Quantidade disponível de leite veg. em mililitros (ml).
    m (int): Quantidade disponível de mate em mililitros (g).
    cc (int): Quantidade disponível de calda de chocolate em mililitros (ml).
    Q_GELO (int): Quantidade de gelo necessária para o preparo das bebidas (un).
    id (int): ID da bebida que está sendo vendida.

    Retorno:
    int: Nova quantidade disponível de café solúvel em gramas (g).
    int: Nova quantidade disponível de água em mililitros (ml).
    int: Nova quantidade disponível de cubos de gelo (un).
    int: Nova quantidade disponível de leite em mililitros (ml).
    int: Nova quantidade disponível de leite veg. em mililitros (ml).
    int: Nova quantidade disponível de mate em mililitros (g).
    int: Nova quantidade disponível de calda de chocolate em mililitros (ml).
    float: Valor da bebida.
    """
    #Variaveis de cores
    WHITE = '\033[37m'
    BWHITE = '\033[97m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'

    fL = lambda op1, op2, id: op1 if (id != 0) else op2 #Faz a concordância de gênero entre as bebidas e os textos

    space, nB, v, cB, aB, leB, mB, ccB, gelada = fDict(id) #Item de fDict
    SPACE = (16 + (space * -1)) #Espaços para o formatar a venda

    #Tela de Venda
    print(f"+{'-' * (SPACE + 2)}+") #Cabeçalho +---+
    print(f"| Você escolheu {fL('o', 'a', id)} {PURPLE}{nB}{WHITE} |")
    print(f"| {' ' * fSpace(v, 10+3, SPACE)}Preço: {GREEN}R$ {v:.2f}{WHITE}{' ' * fSpace(v, 10+3, SPACE, True)} |")
    print(f"+{'-' * (SPACE + 2)}+", end = "")

    if ((gelada > 1) and (g - Q_GELO >= 0)): #Se for gelada opcional e tiver gelo disponível
        txt = f"\nDeseja que {fL('seu', 'sua', id)} {PURPLE}{nB}{WHITE} seja\npreparad{fL('o', 'a', id)} {RED}{fL('Quente', 'Tmp. Natural', id)} (1) {WHITE}ou {CYAN}Gelad{fL('o', 'a', id)} (2){WHITE}? "
        rsp = Rinput(int, 2, txt, f"{YELLOW}Por favor, utilize apenas os números {RED}1 {YELLOW}e {CYAN}2{YELLOW}.{WHITE}")
        g -= Q_GELO if (rsp == 2) else 0
    elif (gelada == 1): #Se for gelada obrigatória
        g -= Q_GELO

    if((leB > 0) and ((l - leB) >= 0) and ((lv - leB) >= 0)): #Se precisar de leite e tiver leite comum e vegetal
        txt = f"\nDeseja que seu {PURPLE}{nB}{WHITE} seja\npreparado com {BWHITE}Leite Comum (1) {WHITE}ou com\n{GREEN}Leite Vegetal (2){WHITE}? "
        rsp = Rinput(int, 2, txt, f"{YELLOW}Por favor, utilize apenas os números {BWHITE}1 {YELLOW}e {GREEN}2{YELLOW}.{WHITE}")
        l, lv = ((l - leB), lv) if (rsp == 1) else (l, (lv - leB)) #Atualizará somente a variável correta com base na seleção acima
    elif((leB > 0) and ((l - leB) >= 0)): #Se precisar de leite e só tiver leite comum
        l -= leB
    elif((leB > 0) and ((lv - leB) >= 0)): #Se precisar de leite e só tiver leite vegetal
        lv -= leB
    
    print("")

    return (c - cB), (a - aB), g, l, lv, (m - mB), (cc - ccB), v

def pix(v):
    """
    Função responsável por receber o pagamento.

    Paramentro:
    v (float): Valor que precisamos receber.

    Retorno:
    float: Valor que deverá ser devolvido como troco.
    """
    #Variaveis de cores
    WHITE = '\033[37m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'

    rsp = Rinput(float, 94000.00, f"{WHITE}Insira o dinheiro (em R$): {GREEN}", f"{YELLOW}Por favor, utilize apenas os números entre {GREEN}0.01 {YELLOW}e {GREEN}94000{YELLOW}.{WHITE}", 0.01)
    
    print(WHITE, end = "")

    dif = round(rsp - v, 2) #Diferença arredondada em duas casas

    if (dif >= 0): 
        return dif

    return pix(round(v - rsp, 2)) #Se a diferença não for maior ou igual a 0 -que simboliza que o valor inserido é maior ou igual o necessário-, chamará uma recursão

def m1(c, a, g, l, lv, m, cc, Q_GELO, off, i = 1):
    """
    Função responsável por verificar se tem, ao menos, 
    um item, que pode ser produzido, depois do último 
    mostrado no menu, para que mostre, se verdadeiro, 
    a opção de próxima página.

    Parametro:
    c (int): Quantidade disponível de café solúvel em gramas (g).
    a (int): Quantidade disponível de água em mililitros (ml).
    g (int): Quantidade disponível de cubos de gelo (un).
    l (int): Quantidade disponível de leite em mililitros (ml).
    lv (int): Quantidade disponível de leite veg. em mililitros (ml).
    m (int): Quantidade disponível de mate em mililitros (g).
    cc (int): Quantidade disponível de calda de chocolate em mililitros (ml).
    Q_GELO (int): Quantidade de gelo necessária para o preparo das bebidas (un).
    off (int)(opc): Indica em qual menu estar (offset).
    i (int)(opc): Contador responsável por determinar o item de fDict() da iteração.

    Retorno:
    bool: True, caso tenha algum item disponível, se não, False.
    """
    vf = lambda x, y, z = None: (y - x if (z == None) else z - y) if (x) else None #Caso x != 0, analizará z que se for != none responderá z-y, se não y-x. Isso é usado para mandar as diferenças para check.

    space, nB, v, cB, aB, leB, mB, ccB, gelada = fDict(i + off) #Pega um item de fDict

    if (nB != None):
        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB)
        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))): #Se a bebida puder ser produzida
            return True
        else:
            return m1(c, a, g, l, lv, m, cc, Q_GELO, off, i + 1) #Caso não posso, chama a recursão
    else: #Se não acharmos nenhum disponível até a água (0), verificaremos esse 
        space, nB, v, cB, aB, leB, mB, ccB, gelada = fDict(0) #água
        bo, uG, uL, uLV = check(c - cB, a - aB, vf(gelada, Q_GELO, g), vf(leB, l), vf(leB, lv), m - mB, cc-ccB)
        if (bo and (gelada != 1 or (gelada == 1 and uG)) and (not leB or (leB and (uL or uLV)))):
            return True #Caso seja possível produzir a Água c/ Gelo
    
    return False #Caso nenhuma seja verdadeira, retornará false

def fSpace(nM, r, s, f = False):
    """
    Função responsável por calcular quantos espaços em branco devem ser dados.

    Paramentros:
    nM (int) (None): Número que tem que ser menor que 10; Se None, 
        não ira subtrair nada além de r.
    r (int): Número que deve ser removido dos espaços além de 
        2 (para >= 10), 1 (para < 10) ou 0 (para None).
    s (int): Espaços disponíveis.
    f (bool)(opc): Indica se estamos no espaço da direita da frase. É usada quando
        os espaços restantes não forem divisíveis por 2.

    Retorna:
    int: Quantidade de espaços em branco.
    """
    space2 = lambda y, f: (y//2) if (not f) else ((y//2) if (y % 2 == 0) else ((y//2) + 1)) #Verifica se estamos nos tratando do espaço à direita.
    #v Se nM == none manda para função acima os valores de espaço (total - o que estamos usando), se não, caso for maior igual a 10, manda os valores de espaço -1, se não, -2. Após todas essas considerações, os valores são retornados. 
    return (space2((s - r), f)) if (nM == None) else (space2((s - 2 - r), f)) if ((nM) >= 10) else (space2((s - 1 - r), f))

def p1(n1, qL, SPACES, msg):
    """
    Função para imprimir as 'Outras Opções'

    Parametros:
    n1 (int): Número que indica a função.
    qL (int): Quantidade de letras da frase da opção.
    SPACES (int): Constante que indica a quantidade de espaços
        que o menu possui.
    msg (str): String com a frase da opção.

    Retorno: None
    """
    print(f"|{' ' * fSpace(n1, qL, SPACES)}", end = "")
    print(f"{n1}{msg}", end = "")
    print(f"{' ' * fSpace(n1, qL, SPACES, True)}|")

    return

def programa(cup, c, a, g, l, lv, m, cc, off = 0, fat = 0):
    """
    Função responsável pela execução do programa.

    Parametros:
    cup (int): Quantidade disponível de copos (un).
    c (int): Quantidade disponível de café solúvel em gramas (g).
    a (int): Quantidade disponível de água em mililitros (ml).
    g (int): Quantidade disponível de cubos de gelo (un).
    l (int): Quantidade disponível de leite em mililitros (ml).
    lv (int): Quantidade disponível de leite veg. em mililitros (ml).
    m (int): Quantidade disponível de mate em mililitros (g).
    cc (int): Quantidade disponível de calda de chocolate em mililitros (ml).
    off (int)(opc): Indica em qual menu estar (offset).
    fat (int)(opc): Faturamento (R$).

    Retorno: None
    """
    #Variáveis de cor
    WHITE = '\033[37m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BWHITE = '\033[97m'

    SPACES = 55 #Espaços para o formatar o menu
    Q_GELO = 5 #Quantidade de gelo necessaria para o preparo das bebidas geladas

    limpa()
    lch = lambda vl, v1, v2, v3, v4, v5: (v1 != vl and v2 != vl and v3 != vl and v4 != vl and v5 != vl) 
    #^ Função para verificar se valores entre duas variáveis são iguais, usada para 0 e none para saber se continuaremos o menu

    soma = lambda var: 1 if (var != None) else 0 #Usada para saber se temos algum ingrediente em falta

    next = 0

    #Menu
    print(f"+{'-' * SPACES}+") #Cabeçalho +----+
    print(f"| OPÇÃO |{' ' * 7}PRODUTO E VARIANTES*{' ' * 7}| PREÇO (un) |")
    print(f"+{'-' * SPACES}+")
    print(f"|{' ' * 23}*Legenda:{' ' * 23}|")
    print(f"|{' ' * 7}{CYAN}(G){WHITE} -> Pode ser, ou é**, preparada gelada{' ' * 7}|")
    print(f"|{' ' * 8}**Confira em 'Informações dos Produtos'{' ' * 8}|")
    print(f"|{' ' * 7}{BWHITE}(L){WHITE} -> Pode ser preparada com leite comum{' ' * 7}|")
    print(f"|{' ' * 6}{GREEN}(V){WHITE} -> Pode ser preparada com leite vegetal{' ' * 6}|")
    print(f"+{'-' * SPACES}+")
    #Menu

    id1, id2, id3, id4, id5 = menu(cup, c, a, g, l, lv, m, cc, Q_GELO, off) #Menu e os ids de cada item que o compõe

    fIng = (id1 == id2 == id3 == id4 == id5 == None) #Variável usada para saber se o menu não está vazio

    if ((cup > 0) and (not fIng)):
        print(f"+{'-' * SPACES}+")
        next = 5 if (id5 != None) else 4 if (id4 != None) else 3 if (id3 != None) else 2 if (id2 != None) else 1 if (id1 != None) else 0 #Variável que dá o offset caso tenha

        if (lch(0, id1, id2, id3, id4, id5) and lch(None, id1, id2, id3, id4, id5)):
            ck = m1(c, a, g, l, lv, m, cc, Q_GELO, id5)
            
            if (off >= 5):
                next += 1
                print(f"|{' ' * 18}{next} - Página Anterior{' ' * 18}|")
                print(f"+{'-' * SPACES}+")
            if (ck):
                next += 1
                print(f"|{' ' * 18}{next} - Próxima Página{' ' * 19}|")
                print(f"+{'-' * SPACES}+")

        elif (off >= 5):
            next += 1
            print(f"|{' ' * 18}{next} - Página Anterior{' ' * 18}|")
            print(f"+{'-' * SPACES}+")
    else:#
        fg = 0

        #v Manutenção
        print(f"|{' ' * fSpace(None, 22, SPACES)}Aguardando Manutenção!{' ' * fSpace(None, 22, SPACES, True)}|")
        print(f"|{' ' * fSpace(None, 14, SPACES)}Falta de copo!{' ' * fSpace(None, 14, SPACES, True)}|") if (cup <= 0) else None
        print(f"|{' ' * fSpace(None, 22, SPACES)}Falta de ingredientes:{' ' * fSpace(None, 22, SPACES, True)}|") if (fIng) else None
        
        _, __, ___, cBx, aBx, leBx, mBx, ccBx, ____ = fDict(-1) #Recebe os menores valores de cada ingrediente que são usados nas bebidas
        var = print(f"|{' ' * fSpace(None, 14, SPACES)}- Café Solúvel{' ' * fSpace(None, 14, SPACES, True)}|") if (c < cBx) else True
        fg += soma(var) #Realiza a soma para no final saber se precisará imprimir 'nenhum'
        var = print(f"|{' ' * fSpace(None, 6, SPACES)}- Água{' ' * fSpace(None, 6, SPACES, True)}|") if (a < aBx) else True
        fg += soma(var)
        var = print(f"|{' ' * fSpace(None, 6, SPACES)}- Gelo{' ' * fSpace(None, 6, SPACES, True)}|") if (g < Q_GELO) else True
        fg += soma(var)
        var = print(f"|{' ' * fSpace(None, 13, SPACES)}- Leite Comum{' ' * fSpace(None, 13, SPACES, True)}|") if (l < leBx) else True
        fg += soma(var)
        var = print(f"|{' ' * fSpace(None, 15, SPACES)}- Leite Vegetal{' ' * fSpace(None, 15, SPACES, True)}|") if (lv < leBx) else True
        fg += soma(var)
        var = print(f"|{' ' * fSpace(None, 25, SPACES)}- Preparado para Chá-mate{' ' * fSpace(None, 25, SPACES, True)}|") if (m < mBx) else True
        fg += soma(var)
        var = print(f"|{' ' * fSpace(None, 20, SPACES)}- Calda de Chocolate{' ' * fSpace(None, 20, SPACES, True)}|") if (cc < ccBx) else True
        fg += soma(var)

        print(f"|{' ' * fSpace(None, 8, SPACES)}- Nenhum{' ' * fSpace(None, 8, SPACES, True)}|") if (fg >= 7) else None

        print(f"+{'-' * SPACES}+")

    print(f"|{' ' * 20}Outras Opções:{' ' * 21}|")

    p1((next + 1), 27, SPACES, " - Informações dos Produtos")
    p1((next + 2), 23, SPACES, " - Informações Internas")
    p1((next + 3), 12, SPACES, " - Finalizar")   
    print(f"+{'-' * SPACES}+\n")

    q1 = Rinput(int, next + 3, "Digite a opção que deseja: ", f"Por favor, utilize números inteiros de 1-{next+3}.")

    if (((q1 == next == 6) and (off < 5)) or ((q1 == next == 7) and (off >= 5))):  #Faz ir para próxima página
        off = id5
        programa(cup, c, a, g, l, lv, m, cc, off, fat)
    elif ((off >= 5) and (((q1 == next) and (next != 7)) or ((q1 == next - 1) and (next == 7)))): #Faz voltar uma página
        off -= 5
        programa(cup, c, a, g, l, lv, m, cc, off, fat)
    elif (q1 == (next + 1)): #Informação dos Produtos
        limpa()
        print(f"+{'-' * 55}+")
        print(f"|{' ' * fSpace(None, 9, 55)}{PURPLE}Produtos:{WHITE}{' ' * fSpace(None, 9, 55, True)}|")
        infoP(Q_GELO)
    elif (q1 == (next + 2)): #Informações Internas
        limpa()
        infoI(cup, c, a, g, l, lv, m, cc, fat)
    elif (q1 == (next + 3)): #Finaliza
        limpa()
        print(f"+{'-' * 55}+")
        print(f"|{' ' * fSpace(None, 12, 55)}{YELLOW}Finalizando!{WHITE}{' ' * fSpace(None, 12, 55, True)}|")
        infoI(cup, c, a, g, l, lv, m, cc, fat, True)
        exit()
    else: #Tenta vender
        limpa()

        if (q1 == 1): #id1
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id1)
        elif (q1 == 2): #id2
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id2)
        elif (q1 == 3): #id3
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id3)
        elif (q1 == 4): #id4
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id4)
        elif (q1 == 5): #id5
            c, a, g, l, lv, m, cc, v = venda(c, a, g, l, lv, m, cc, Q_GELO, id5)

        cup -= 1
        fat += v

        qtroco = pix(v)
        print(f"\nTroco: {GREEN}R$ {qtroco:.2f}{WHITE}")
        (print(f"\nPegue seu troco: {GREEN}"), troco(qtroco), print(f"{WHITE}")) if (qtroco > 0) else print("")

        txt = f"Deseja comprar outro produto? ({GREEN}Sim (1){WHITE}; {RED}Não (2){WHITE}) "
        rsp = Rinput(int, 2, txt, f"{YELLOW}Por favor, utilize apenas os números {GREEN}1 {YELLOW}e {RED}2{YELLOW}.{WHITE}")
        txt2 = f"|{' ' * fSpace(None, 12, 55)}{YELLOW}Finalizando!{WHITE}{' ' * fSpace(None, 12, 55, True)}|"
        (limpa(), print(f"+{'-' * 55}+"), print(txt2), infoI(cup, c, a, g, l, lv, m, cc, fat, True), exit()) if (rsp == 2) else None
        #^ Se a resposta for não, chamará limpa(), imprimirá 'finalizando!' e chamara infoI -informações internas- e sairá do programa por meio do exit() 
        off = 0 #Sempre volta pra página inicial depois de vender

    programa(cup, c, a, g, l, lv, m, cc, off, fat) #Recursão caso nenhuma seja chamada antes

    return

def main():
    programa(cup = 17, c = 500, a = 3250, g = 45, l = 960, lv = 960, m = 14, cc = 120) #Esse comando roda o sistema
    #         copos,    café,    água,     gelo,   leite, l. vegano, chá mate, calda
    #cup = 17, c = 500, a = 3250, g = 45, l = 960, lv = 960, m = 14, cc = 120
    #^ Configuração para vender 1 de cada opção (incluindo todas permutações de quente/gelado, vegano/comum)

main()