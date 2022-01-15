idade = int(input())

if (idade <= 34): #aqui comeca +5
    tMax = 180
elif (idade <= 39):
    tMax = 185 #+5
elif (idade <= 44):
    tMax = 190 #+5
elif (idade <= 49): #aqui interrompe
    tMax = 200 #+10 -> +5 habitual +5 que tem que ser a mais
elif (idade <= 54):
    tMax = 205 #+5
elif (idade <= 59): #aqui comeca +15
    tMax = 215 #+10
elif (idade <= 64):
    tMax = 230 #+15
elif (idade <= 69):
    tMax = 245 #+15
elif (idade <= 74):
    tMax = 260 #+15
elif (idade <= 79):
    tMax = 275 #+15
else:
    tMax = 290 

print(tMax)

f = lambda idade, i, m: (m * (idade//5 - i//5))

if idade < 34:
    tMax = 180
elif idade >= 80:
    tMax = 290
elif idade <= 54:
    tMax = (180 if idade <= 44 else 180 + 5) + (f(idade, 34, 5))
else:
    tMax = 215 + (f(idade, 59, 15))

print(tMax)