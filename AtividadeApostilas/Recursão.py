from math import pi

def f(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * f(n-1)

def w():
    x = input()
    if (x == "X" or x == "x"):
        return 0
    else:
        return int(x) + w(); 

def x(n, m = 0):
    if (n == 0):
        print(0)
    else:
        if (m == 1):
            x(n-1, m)
            print(n)
        else:
            print(n)
            x(n-1, m)

def v():
    r = float(input())
    print(f"Volume: {(4/3)*pi*r**2}")
    resp = input()
    if resp == "N" or resp == "n":
        exit()
    else:
        v()

def main():
    #n = int(input())
    #fr = f(n)
    #print(fr if fr > 0 else "ERRO")
    #print(w())
    #x(10, 1)
    #print("\n")
    #x(10, 0)
    v()

main();