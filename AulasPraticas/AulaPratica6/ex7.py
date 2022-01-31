def desenha1(n, c = "*", i = 1):
    if i <= n:
        print(c*n)
        desenha1(n, c, i + 1)

def desenha2(n, c = "*", i = 1):
    if i <= n:
        print(c*i)
        desenha2(n, c, i + 1)

def desenha3(n, c = "*", i = 1):
    if n % 2 == 0:
        print("n deve ser impar")
    if i <= n:
        ne = (n-i)//2
        print(" "*ne + c*i)
        desenha3(n, c, i + 2)

desenha1(5) #-> quadrado
print("\n") 
desenha2(5) #-> triangulo retangulo
print("\n")
desenha3(5) #-> piramide alinhada