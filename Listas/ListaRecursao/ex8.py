def fac(x):
    if (x == 0):
        return 1
    else:
        return x * fac(x-1)

def euler(x, q = 0, f = fac):
    if ((x-1) == q):
        return 1/f(q)
    else:
        return 1/f(q) + euler(x, q+1)

def main():
    t = int(input())
    if t < 0:
        print("ERRO!")
    else:
        r = euler(t)
        print(f"Resultado: {r}")
main()