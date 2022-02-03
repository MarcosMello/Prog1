######################################################
# Programação Funcional / Programção I (2021/2)
# miniEP6 - Avatar: A Lenda de Aang
# Nome: Marcos Vinicius Vargas Mello
# Matrícula: 2021200102
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional;
# - Você não pode usar variáveis globais;
# - Caso precise, você PODE criar outras funções;
# - Você PODE adicionar os parâmetros que achar 
#   necessários na função 'realizaTreinamentoAvatar'.
######################################################

def realizaTreinamentoAvatar(a = 0, t = 0, f = 0, ar = 0, i = 0):
    calc2 = lambda n: n if (n >= 0) else 0
    calc = lambda el1, el2, p: (el1 + p, calc2(el2 - (p/2))) if (el2 > 0) else (el1 + p, el2)

    el = input()

    if el != "FIM":
        pts = int(input())

        if (el == "AGUA"):
            a, f = calc(a, f, pts)
        elif (el == "TERRA"):
            t, ar = calc(t, ar, pts)
        elif (el == "FOGO"):
            f, a = calc(f, a, pts)
        elif (el == "AR"):
            ar, t = calc(ar, t, pts)
        
        a, t, f, ar = realizaTreinamentoAvatar(a, t, f, ar, i + 1)
    
    if (i == 0):
        print("Pontuacao Final")
        print(f"Agua: {a:.1f}")
        print(f"Terra: {t:.1f}")
        print(f"Fogo: {f:.1f}")
        print(f"Ar: {ar:.1f}")

        return a and t and f and ar
    
    return a, t, f, ar
    
######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    treinamentoAvatar = realizaTreinamentoAvatar()
    if treinamentoAvatar == True:
        print("Treinamento realizado com sucesso.")
    elif treinamentoAvatar == False:
        print("Realize mais treinamentos.")
    else:
        print("ERRO: A implementação da função 'realizaTreinamentoAvatar' possui algum erro")

main()
