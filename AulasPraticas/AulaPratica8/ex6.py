def procura(L, x):
    return (True) if (x in L) else (False)

def main():
    disciplinasFeitas = ["Cálculo 1", "Programação I", "Algebra linear", "Circuitos 1", "Estrutura de Dados 1"]
    
    print(disciplinasFeitas)
    x = "Cálculo 1"
    if procura(disciplinasFeitas, x):
        print(f"Aluno já fez '{x}'")
    else:
        print(f"Aluno ainda não fez '{x}'")
        
    x = "Estrutura de Dados 1"
    if procura(disciplinasFeitas, x):
        print(f"Aluno já fez '{x}'")
    else:
        print(f"Aluno ainda não fez '{x}'")

    x = "Cálculo 2"
    if procura(disciplinasFeitas, x):
        print(f"Aluno já fez '{x}'")
    else:
        print(f"Aluno ainda não fez '{x}'")


    x = "Estrutura de Dados 2"
    if procura(disciplinasFeitas, x):
        print(f"Aluno já fez '{x}'")
    else:
        print(f"Aluno ainda não fez '{x}'")

    lista = [2, 3, 5, 7, 11]
    print(lista)
    x = 7
    if procura(lista, x):
        print(f"{x} está na lista")
    else:
        print(f"{x} não está na lista")

    x = 25
    if procura(lista, x):
        print(f"{x} está na lista")
    else:
        print(f"{x} não está na lista")


    lista2 = [1, 2, "UFES", "CEUNES"]
    print(lista2)
    x = 3.5
    if procura(lista2, x):
        print(f"{x} está na lista")
    else:
        print(f"{x} não está na lista")

    x = "UFES"
    if procura(lista2, x):
        print(f"{x} está na lista")
    else:
        print(f"{x} não está na lista")

main()