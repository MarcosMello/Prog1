ok = True

peso = float(input())
idade = int(input())
if (16 <= idade < 18):
    doc = input()
saude = input()
drogas = input()
primeira = input()
if (primeira == "N"):
    meses = int(input())
    ultimas = int(input())
sexob = input()
if (sexob == "F"):
    gravida = input()
    amamentando = input()
    if (amamentando == "S"):
       idadebb = int(input())

print(f"Peso: {peso}")
print(f"Idade: {idade}")
if (16 <= idade < 18): 
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
    if (amamentando == "S"):
        print(f"Meses bebe: {idadebb}")

if (peso < 50):
    print("Impedimento: abaixo do peso minimo.")
    ok = False
if (16 > idade):
    print("Impedimento: menor de 16 anos.")
    ok = False
elif (idade > 60 and primeira == "S"):
    print("Impedimento: maior de 60 anos, primeira doacao.")
    ok = False
elif ((16 <= idade < 18) and (doc == "N")):
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    ok = False
elif (idade > 69):
    print("Impedimento: maior de 69 anos.")
    ok = False
if (saude == "N"):
    print("Impedimento: nao esta em boa saude.")
    ok = False
if (drogas == "S"):
    print("Impedimento: uso de drogas injetaveis.")
    ok = False
if ((primeira == "N") and ((sexob == "M" and meses < 2) or (sexob == "F" and meses < 3))):
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    ok = False
if ((primeira == "N") and ((sexob == "M" and ultimas >= 2) or (sexob == "F" and ultimas >= 3))):
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    ok = False
if ((sexob == "F") and (gravida == "S")):
    print("Impedimento: gravidez.")
    ok = False
if ((sexob == "F") and (amamentando == "S") and (idadebb < 12)):
    print("Impedimento: amamentacao.")
    ok = False

if (ok):
    print("Procure um hemocentro.")