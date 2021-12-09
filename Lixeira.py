ok = True
doc = "-"

peso = float(input())
if (peso < 50):
    ok = False
idade = int(input())
if (16 > idade):
    ok = False
elif (idade < 18):
    doc = input()
    if (doc == "N"):
        ok = False
elif (idade > 69):
    ok = False
saude = input()
if (saude == "N"):
    ok = False
drogas = input()
if (drogas == "S"):
    ok = False
primeira = input()
if (primeira == "S"):
    if (idade > 60):
        ok = False
else:
    meses = int(input())
    ultimas = int(input())
sexob = input()

if (sexob == "F"):
    gravida = input()
    if (gravida == "S"):
        ok = False
    amamentando = input()
    if (amamentando == "S"):
       idadebb = int(input())
       if (idadebb < 12):
           ok = False
    if ((primeira == "N") and (meses < 3) and (ultimas >= 3)):
        ok = False
else:
    if ((primeira == "N") and (meses < 2) and (ultimas >= 4)):
        ok = False 

print(f"Peso: {peso}")
print(f"Idade: {idade}")
if (doc != "-"): 
    print(f"Documento de autorizacao: {doc}")
print(f"Boa saude: {saude}")
print(f"Uso drogas injetaveis: {drogas}")
print(f"Primeira doacao: {primeira}")
if (primeira == "N"):
    print(f"Meses desde ultima doacao: {meses}")
    print(f"Doacoes nos ultimos 12 meses: {ultimas}")
print(f"Sexo biologico: {sexob}")
if (sexob == "F"):
    print(f"Gravidez: {gravida}")
    print(f"Amamentando: {amamentando}")
    if(amamentando == "S"):
        print(f"Meses bebe: {idadebb}")

if (ok):
    print("Procure um hemocentro.")
else:
    if (peso < 50):
        print("Impedimento: abaixo do peso minimo.")
    if (16 > idade):
        print("Impedimento: menor de 16 anos.")
    elif (idade > 60 and primeira == "S"):
        print("Impedimento: maior de 60 anos, primeira doacao.")
    elif (doc != "-" and doc == "N"):
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    elif (idade > 69):
        print("Impedimento: maior de 69 anos.")
    if (saude == "N"):
        print("Impedimento: nao esta em boa saude.")
    if (drogas == "S"):
        print("Impedimento: uso de drogas injetaveis.")
    if ((primeira == "N") and ((sexob == "M" and meses < 2) or (sexob == "F" and meses < 3))):
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    if ((primeira == "N") and ((sexob == "M" and ultimas >= 2) or (sexob == "F" and ultimas >= 3))):
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    if ((sexob == "F") and (gravida == "S")):
        print("Impedimento: gravidez.")
    if ((amamentando == "S") and (idadebb < 12)):
        print("Impedimento: amamentacao.")