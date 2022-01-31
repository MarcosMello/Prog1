def countS(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    x, o, s = 0, 0, 0 

    fxo = lambda p, x, o, s: (x + 1, o, s) if (p == "x") else (x, o + 1, s) if (p == "o") else (x, o, s)
    f = lambda p, x, o, s: (x, o, s + 1) if (p == " ") else (fxo(p, x, o, s))

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

def cond(p, x, o, s):
    if (p == " "):
        return (x, o, s + 1)
    elif (p == "x"):
        return (x + 1, o, s)
    elif (p == "o"):
        return (x, o + 1, s)
    else:
        return (x, o, s)
    

#((x + 1, o, s) if (p == "x") else (x, o + 1, s) if (p == "o") else (x, o, s)) if (p != " ") else (x, o, s + 1)
fs = lambda p, s: (s + 1) if (p == " ") else (s)
f = lambda p, x, o, s: ((x + 1, o, s) if (p == "x") else (x, o + 1, s) if (p == "o") else (x, o, s)) if (p != " ") else (x, o, s + 1)

f = lambda p, x, o, s: (x, o, s + 1) if (p == " ") else (fxo(p, x, o, s))
fxo = lambda p, x, o, s: (x + 1, o, s) if (p == "x") else (x, o + 1, s) if (p == "o") else (x, o, s) 



#situação de ganhar = (n de peças v > n de peças p)

p1 = input()
p2 = input()
p3 = input()
p4 = input()
p5 = input()
p6 = input()
p7 = input()
p8 = input()
p9 = input()

s = 0

if (p1 == p2 == p3 != " "): #- 
    print(f"O jogador '{p1}' venceu!")    
elif (p4 == p5 == p6 != " "): #-
    print(f"O jogador '{p4}' venceu!")
elif (p7 == p8 == p9 != " "): #-
    print(f"O jogador '{p7}' venceu!")
elif (p7 == p4 == p1 != " "): #|
    print(f"O jogador '{p7}' venceu!")
elif (p8 == p5 == p2 != " "): #|
    print(f"O jogador '{p8}' venceu!")
elif (p9 == p6 == p3 != " "): #|
    print(f"O jogador '{p9}' venceu!")
elif (p7 == p5 == p3 != " "): #\
    print(f"O jogador '{p7}' venceu!")
elif (p1 == p5 == p9 != " "): #/
    print(f"O jogador '{p1}' venceu!")
elif (s == 0):
    print("Empate!")
else:
    print("O jogo nao terminou!")
