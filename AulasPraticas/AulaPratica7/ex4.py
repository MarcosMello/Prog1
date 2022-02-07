def P(n, nd = 0, i = 1): #numeros primos
    if n <= 1:
        return False
    if i == n:
        nd += 1 #representa o n de divisores
        return True if nd == 2 else False
    else:
        if n%i == 0:
            return P(n, nd+1, i+1)
        else:
            return P(n, nd, i+1)

def primos(n, i = 2): #sem nd
    if n == i:
        return True
    
    if n % i == 0 or n == 1:
        return False
    
    return primos(n, i + 1)

def main():
    print("1 = ", primos(1))
    print("2 = ", primos(2))
    print("3 = ", primos(3))
    print("4 = ", primos(4))
    print("5 = ", primos(5))
    print("6 = ", primos(6))
    print("7 = ", primos(7))
    print("8 = ", primos(8))
    print("9 = ", primos(9))
    print("10 = ", primos(10))
    print("13 = ", primos(13))
    #Faça outros testes

main()