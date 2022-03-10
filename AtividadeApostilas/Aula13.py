def vazia(L):
    return True if (len(L) == 0) else False

def divisores(n, i = 1, L = []):
    if n >= i:
        if n%i == 0:
            return divisores(n, i + 1, L + [i])
        return divisores(n, i + 1, L)
    return L

def mMap(f, L, R = [], i = 0):
    if len(L) != i:
        try:
            R += [f(L[i])]
            return mMap(f, L, R, i + 1)
        except:
            return mMap(f, L, R, i + 1)
    return R

def filtro(L, R = [], i = 0):
    if (i < len(L)):
        if (type(L[i]) == int):
            return filtro(L, R + [L[i]], i + 1)
        return filtro(L, R, i + 1)
    return R

def main():
    print(vazia([]))
    print(vazia([1, 2, 3]))
    print(divisores(7))
    print(mMap(int, ["1", "2", "3", "45", "100"]))
    print(filtro(["1", True, 2, 1, "11"]))

main()