from math import factorial as fac, comb as cb

def main():
    n = int(input("N: "))
    p = int(input("P: "))

    if (p <= n):
        comb(n, p) #minha funcao
        #print(f"Cb = {cb(n, p)}.") #funcao de combinacao da lib math 
    else:
        print("Erro")

def comb(n, p):
    c = fac(n) / (fac(n-p) * fac(p))
    print(f"C = {c}.")

main()