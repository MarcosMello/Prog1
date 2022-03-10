def divisores(n, L=[], i=1):
    if i <= n:
        if n % i == 0:
            return divisores(n, L + [i], i + 1)
        else:
            return divisores(n, L, i + 1)
    else:
        return L

def main():
    L = [x for x in range(31) if len(divisores(x)) == 2]
    print(L)

main()