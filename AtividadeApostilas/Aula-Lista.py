def lNotas(qt = 0, sm = 0):
    try:
        l = float(input(""))
    except:
        print("ERRO!")
        return lNotas(qt, sm)

    if l <= 0:
        return qt, sm, (sm/qt)
    
    return lNotas(qt + 1, sm + l)

qt, sm, med = lNotas()

print(f"Quantidade: {qt}\nSoma: {sm}\nMédia: {med:.2f}")