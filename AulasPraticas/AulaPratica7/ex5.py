def b(n): #retorna numeros binarios em str
    if type(n) != int or n < 0: #n deve ser um número natural
        print("ERRO: O argumento deve ser inteiro positivo")
        return None
    elif n < 2: #Você consegue pensar em uma forma de simplificar essa parte?
        return str(n % 2)
    else: #Você consegue pensar em uma forma de simplificar o return?
         return b(n//2) + str(n % 2)

def main():
    print("b(1) =", b(1))
    print("b(2) =", b(2))
    print("b(3) =", b(3))
    print("b(4) =", b(4))
    print("b(5) =", b(5))
    print("b(6) =", b(6))
    print("b(7) =", b(7))
    print("b(8) =", b(8))
    print("b(9) =", b(9))
    print("b(10) =", b(10))
    #Faça outros testes

main()

#o número binario ficará invertido
#se usarmos n%1 == 0 teremos erro quando for string