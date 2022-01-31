def f1(n, i=0, soma=0):
   if i <= n:
       return f1(n, i+1, soma+i)
   else:
       return soma

def imprimeSoma(n):
    if n > 0:
        imprimeSoma(n - 1)
        print(f"{n} = {f1(n)}")

def main():
    print(f"A Soma dos valores até 10 é {f1(10)}")
    print(f"A Soma dos valores até 5 é {f1(5)}")
    print(f"A Soma dos valores até 20 é {f1(20)}\n")

    imprimeSoma(5)

main()