def palin(se = 1, mid = 0):
    print(f"{se}{mid}{mid}{se}")

    if ((se == 9) and (mid == 9)):
        return None
    elif (mid == 9): 
        mid = 0
        se += 1

        return palin(se, mid)
    else:
        mid += 1

        return palin(se, mid)

def printnum(n, i = 0):
    print(i)

    if (i == abs(n)):
        return None
    else:
        i += 1

        return printnum(n, i)

def interval(a, b, c = 0, flag = False):
    if (not flag):
        c = a

        return interval(a, b, c, flag = True)
    
    c += 1

    if (c < b):
        print(c)

        return interval(a, b, c, flag)

def dPow(a, b):
    if (b == 1):
        return a
    else:
        b -= 1

        return a * dPow(a, b)  

def div(n, c = 1):
    if (n != 0):
        v = 0

        if (n == c):
            return 1
        else:
            if (n % c == 0):
                v = 1
            
            return v + div(n, c+1)
    else:
        return 0

def primo(n, c = 2):
    if (n != 0):
        if (n == c and n != 2):
            return True
        else:
            if (n % c == 0):
                return False
            else:
                return primo(n, c+1)
    else:
        return False

def somaDigitos(n):
    n = abs(n)

    if n < 10:
        return n;
    else:
        return (n - (n//10 * 10)) + somaDigitos(n//10)

def main():
    #palin()
    #printnum(10)
    #interval(-1, 11)
    #print(dPow(3, 3))
    #print(div(7))
    #print(primo(2))
    print(somaDigitos(12345));

main()