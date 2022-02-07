def f1(n):
    """Retorna a quantidade de números naturais pares menores ou iguais a n"""
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return 1 + f1(n - 2) #Por que n - 2? se o n for par (par - 2 = par )
        else:
            return f1(n - 1) #Por que n - 1? se o n for impar (impar - 1 = par)
def f2(n):
    """Retorna a soma dos números naturais menores ou iguais a n"""
    return 1 if n == 1 else n + f2(n - 1)

print(f1(10))
#print(f2(5))