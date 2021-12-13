isAAllowed = True #queremos true
m60P = False #mais de 60 primeira vez - queremos false
isGravida = False #queremos false
bebeM12 = False #idade bebe menor 12 meses - queremos false
isMAllowed = True #queremos true, caso nao possa será corrigido apos
isUAllowed = True #queremos true, caso nao possa será corrigido apos

d_a = "-"

peso = float(input())
idade = int(input())

if (16 <= idade < 18):
    d_a = input()

    if (d_a == "N"):
        isAAllowed = False

saude = input()
drogas = input()
primeira = input()

if (primeira == "N"):
    meses = int(input())
    ultimas = int(input())
else:
    if (idade > 60):
        m60P = True

sexob = input()

if (sexob == "F"):
    gravida = input()

    if (gravida == "S"):
        isGravida = True
    
    amamentando = input()
    if (amamentando == "S"):
        idadeb = int(input())

        if (idadeb < 12):
            bebeM12 = True
        
        print(f"Peso: {peso}")
        print(f"Idade: {idade}")
        if (d_a != "-"): 
            print(f"Documento de autorizacao: {d_a}")
        print(f"Boa saude: {saude}")
        print(f"Uso drogas injetaveis: {drogas}")
        print(f"Primeira doacao: {primeira}")
        if (primeira == "N"):
            print(f"Meses desde ultima doacao: {meses}")
            print(f"Doacoes nos ultimos 12 meses: {ultimas}")
        print(f"Sexo biologico: {sexob}")
        print(f"Gravidez: {gravida}")
        print(f"Amamentando: {amamentando}")
        print(f"Meses bebe: {idadeb}")

    else:
        print(f"Peso: {peso}")
        print(f"Idade: {idade}")
        if (d_a != "-"): 
            print(f"Documento de autorizacao: {d_a}")
        print(f"Boa saude: {saude}")
        print(f"Uso drogas injetaveis: {drogas}")
        print(f"Primeira doacao: {primeira}")
        if (primeira == "N"):
            print(f"Meses desde ultima doacao: {meses}")
            print(f"Doacoes nos ultimos 12 meses: {ultimas}")
        print(f"Sexo biologico: {sexob}")
        print(f"Gravidez: {gravida}")
        print(f"Amamentando: {amamentando}")

    if(primeira == "N"):
        if (meses < 3):
            isMAllowed = False
        if (ultimas >= 3):
            isUAllowed = False

else:
    print(f"Peso: {peso}")
    print(f"Idade: {idade}")
    if (d_a != "-"): 
        print(f"Documento de autorizacao: {d_a}")
    print(f"Boa saude: {saude}")
    print(f"Uso drogas injetaveis: {drogas}")
    print(f"Primeira doacao: {primeira}")
    if (primeira == "N"):
        print(f"Meses desde ultima doacao: {meses}")
        print(f"Doacoes nos ultimos 12 meses: {ultimas}")
    print(f"Sexo biologico: {sexob}")

    if (primeira == "N"):
        if (meses < 2): 
            isMAllowed = False
        if (ultimas >= 4):
            isUAllowed = False

if ((peso >= 50) and (16 <= idade <= 69) and (isAAllowed) 
and (not m60P) and (saude == "S") and (drogas == "N") and (isMAllowed) and (isUAllowed) 
and (not isGravida) and (not bebeM12)):
    print("Procure um hemocentro.")
else:
    if (peso < 50):
        print("Impedimento: abaixo do peso minimo.")

    if (16 > idade):
        print("Impedimento: menor de 16 anos.")
    elif (m60P):
        print("Impedimento: maior de 60 anos, primeira doacao.")
    elif (not isAAllowed):
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    elif (idade > 69):
        print("Impedimento: maior de 69 anos.")

    if (saude == "N"):
        print("Impedimento: nao esta em boa saude.")
    if (drogas == "S"):
        print("Impedimento: uso de drogas injetaveis.")
    if ((primeira == "N") and (not isMAllowed)):
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    if ((primeira == "N") and (not isUAllowed)):
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    if (isGravida):
        print("Impedimento: gravidez.")
    if (bebeM12):
        print("Impedimento: amamentacao.")