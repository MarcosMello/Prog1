def concatena(L, i = 0, s = ""): #Se s = 0 não funcionará, porém se for "" ou "0" funcionará, pois é str + str.
    if i < len(L):
        if (type(L[i]) == str):
            return concatena(L, i + 1, s + L[i])
        
        return concatena(L, i + 1, s)
    else:    
        return s

def main():
    lista = ["1", "0", "1", "1", "0"]
    resultado = concatena(lista)
    print(resultado)

main()