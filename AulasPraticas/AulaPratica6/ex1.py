def fatorial(n):
    valido = lambda n: True if ((n >= 0) and (type(n) == int)) else False

    return (1 if n == 0 or n == 1 else n * fatorial(n-1)) if valido(n) else "Erro!"
    
def main():
    n = 2.5
    print(f"{n}! = {fatorial(n)}")
    
    n = -2
    print(f"{n}! = {fatorial(n)}")

    n = 5
    print(f"{n}! = {fatorial(n)}")
    
main()