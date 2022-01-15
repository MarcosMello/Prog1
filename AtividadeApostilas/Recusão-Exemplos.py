""" #EX 1
def f(n, x = 0):
    if n == 2:
        return x + 2
    elif n % 2 == 0:
        x += n;
    
    return f(n-1, x)

def f1(n):
    if n == 2:
        return 2
    elif n % 2 == 1:
        return f(n-1)
    else:
        return n + f(n-1)

print(f(10))
print(f1(10))
"""
""" #EX 2
def conta(n):
    n = abs(n)

    if n < 10:
        return 1;
    else:
        return 1 + conta(n//10)

def somaDigitos(n):
    n = abs(n)

    if n < 10:
        return n;
    else:
        return (n - (n//10 * 10)) + somaDigitos(n//10)


print(conta(-1000))
print(somaDigitos(-123))
"""
""" #EX 3
def f(x):

    if x == 1:
        return 1
    else:
        return x**2 + f(x-1)

print(f(3))
"""
""" #EX 4
def mdc(x,y): #mdc = x // y == z (com resto -> continua, se não para) y/resto ou (y, x%y) 
    if y == 0:
        return x
    else:
        return mdc(y, x%y)

print(mdc(90,36))
"""
""" #EX 4
def m1(n):
    if n == 1:
        return 0
    else:
        return 1 + m1(n//2)

def m2(n):
    if n == 2:
        return 1
    else:
        return 1 + m2(n//2)

print(m1(90))
print(m2(90))
"""
""" #EX 5
def f(x, y = 1):
    if x == y:
        return x
    elif x%y == 0:
        return y + f(x, y+1)
    else:
        return f(x, y+1)

n = 4
x = f(n)
if x == (n+1):
    print("Primo:", end = " ")
else:
    print("Nao e primo:", end = " ")

print(x)
"""
""" #EX 6 - v1
def f(x, y = 1):
    if x == y:
        return x
    elif x%y == 0:
        return y + f(x, y+1)
    else:
        return f(x, y+1)

def ehPerfeito(x, f):
    if ((f(x) - x) == x):
        return True
    else:
        return False

def main():
    print(ehPerfeito(6, f))

main()
"""
#""" #EX6 - v2
def ehPerfeito(x, y = 1, soma = 0):
    if x == y:
        print(soma)
        return True if (soma == x) else False
    elif x%y == 0:
        return ehPerfeito(x, y + 1, soma + y)
    else:
        return ehPerfeito(x, y + 1, soma)

def main():
    print(ehPerfeito(6))

main()
#"""