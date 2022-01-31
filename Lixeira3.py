"""if ((p1 == " ") or (p2 == " ") or (p3 == " ") or (p4 == " ") or (p5 == " ") or (p6 == " ") or (p7 == " ") or (p8 == " ") or (p9 == " ")):
            print("O jogo nao terminou!")"""

"""from LixeiraTestes import countXO

p1 = input()
p2 = input()
p3 = input()
p4 = input()
p5 = input()
p6 = input()
p7 = input()
p8 = input()
p9 = input()

x, o = countXO(p1, p2, p3, p4, p5, p6, p7, p8, p9)

if ((x + o) == 9):
    print("Empate!")
else:
    print("O jogo nao terminou!")""" 

# 1 2 3 -> horizontal 1 em 1
# 7 4 1 -> vertical 3 em 3
# 7 5 3 -> 2 \
# 1 5 9 -> 4 /

f = lambda p: True if (p != " " and p != "x" and p != "o") else False

"""p = " "

e = 1 * (p == " ") + 1 * (p == " ") + 1 * (p == " ") + 1 * (p == " ") + 1 * (p == " ") + 1 * (p == " ") + 1 * (p == " ") + 1 * (p == " ") + 1 * (p == " ")
x = 1 * (p != " ") + 1 * (p != " ") + 1 * (p != " ") + 1 * (p != " ") + 1 * (p != " ") + 1 * (p != " ") + 1 * (p != " ") + 1 * (p != " ") + 1 * (p != " ")

o = (9-e) - x

print(e, x, o)"""

# def ax(a, b):
#     if b == 0:
#         return 0
#     elif b == 1:
#         return a
#     else:
#         return a + ax(a, b-1)

# #print(ax(2,3))

# def x(a):
#     if a == 0:
#         print(0)
#         return
#     else:
#         x(a-1)
#         print(a)

# #x(10)

# def x2(a, b = 0):
#     if a <= b:
#         print(b)
#         x2(a, (b + 1))

# #x2(10)

# def le(n):
#     if n == 0:
#         return 0
#     else:
#         f = int(input())
#         return f + le(n-1)

# #print(le(5))

# def teste(n = 0, soma = 0):
#     k = int(input())

#     if k < 0:
#         return n, soma
#     else:
#         return teste(n+1, k+soma)

# print(teste())

#x, y, z = ((1,2), 2)

# def impar(n):
#     return True if (n%2 == 1) else False

# def impar2(n):
#     return True if (n%2 != 0) else False

# def rec(n, x = 0):
#     if (n == 0):
#         return x
#     else:
#         print(f"Diff de 1 {x}") if (impar(x) != impar2(x)) else None
#         return rec(n - 1, x + 1)

# print(rec(900))

# f = lambda: (1, 2, 3)
# fx = lambda x: f() if (not x) else (3, 2, 1)

# x, y, z = fx(True)

# print(f"{x}{y}{z}")

# fxo = lambda p, x, o, s: (x + 1, o, s) if (p == "x") else (x, o + 1, s) if (p == "o") else (x, o, s) 
# f = lambda p, x, o, s: (x, o, s + 1) if (p == " ") else (fxo(p, x, o, s))

# print(f("x", 0, 0, 0))
# print(f("0", 0, 0, 0))
# print(f(" ", 0, 0, 0))
# print(f("o", 0, 0, 0))

x = "x"
y = "x"
z = "x"

print("A") if (x == y == z != " ") else print("b")