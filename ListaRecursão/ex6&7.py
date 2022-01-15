def qNumber(num):
    if (num < 10):
        return 1
    else:
        return 1 + qNumber(num // 10)

def fac(x, q = 1):
    if (x == 0):
        return 1
    else:
        if (q == x):
            return q
        else:
            return q * fac(x, q + 1) 

def nBi(y, x, fac = fac):
    if (x == 0):
        return 1
    elif (x == 1):
        return y
    else:
        r = fac(y)/(fac(x)*(fac(y - x)))

        return int(r) if ((r - ((r * 10) // 10)) == 0) else r

def xPascal(y, x = 0, s = 1, nBi = nBi, qNumber = qNumber):
    if (y == x):
        print(f"1")
    else:
        num = nBi(y, x)

        print(num, end = (" " * (s - qNumber(num))))
        return xPascal(y, x + 1, s = s)

def yPascal(n, y = 0, xPascal = xPascal, s = 1):
    if (y == (n-1)):
        xPascal(y, s = s)
    else:
        print("  " * (n - (y + 1)), end = "")

        xPascal(y, s = s)
        return yPascal(n, y + 1, s = s)

def main():
    N = 10

    f = lambda x: (x / 2) if (x % 2 == 0) else ((x + 1) / 2)
    yPascal(N, s = (qNumber(nBi(N, f(N))) + 1)) 

main()