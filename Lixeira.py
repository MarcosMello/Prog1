# def getNBeb(i = 0): #falta documentar
#     nB, v, cB, aB, leB, mB, ccB, gelada = fDict(i)

#     if nB == None:
#         return i
    
#     return getNBeb(i + 1)
"""

def troco(res): #falta documentar e escrever uma versão melhor
    if res != 0 and res >= 0.001:
        if res >= 100:
            print("R$ 100.00")
            res -= 100
        elif res >= 50:
            print("R$ 50")
            res -= 50
        elif res >= 20:
            print("R$ 20")
            res -= 20
        elif res >= 10:
            print("R$ 10")
            res -= 10
        elif res >= 5:
            print("R$ 5")
            res -= 5
        elif res >= 2:
            print("R$ 2")
            res -= 2
        elif res >= 1:
            print("R$ 1")
            res -= 1
        elif res >= 0.50:
            print("R$ 0.50")
            res -= 0.50
        elif res >= 0.25:
            print("R$ 0.25")
            res -= 0.25
        elif res >= 0.10:
            print("R$ 0.10")
            res -= 0.10
        elif res >= 0.05:
            print("R$ 0.05")
            res -= 0.05
        elif res >= 0.01:
            print("R$ 0.01")
            res -= 0.01
        troco(res)

    return

"""
"""
m = 10
mult = 100
(f'0,{(f'{m}' if (m >= 10) else f'0{m}')}') 
(f'0,{m}')
(f'{m}' if (m >= 10) else f'0{m}') if(m / mult > 0) else (f'{m},00')
"""