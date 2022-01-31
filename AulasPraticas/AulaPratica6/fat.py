def fatorial(n):
    print(f"Iniciando a função fatorial({n})")
    if n <= 1:
        print(f"Finalizando a função fatorial({n}) com valor 1")
        return 1
    else:
        fat = fatorial(n-1)
        print(f"Finalizando a função fatorial({n}) com valor {n*fat}")
        return n*fat 
        
print("5! =", fatorial(5))