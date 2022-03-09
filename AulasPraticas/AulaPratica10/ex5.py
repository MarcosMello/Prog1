def myMap(f, x, V = []):
    if len(x) == 0:
        return V
    else:
        a = f(x[0])
        return myMap(f, x[1:], V + [a])

def myMapi(f, x, V = [], i = 0):
    if len(x) == i:
        return V
    else: #aqui deveria verificar se cada item atende a função, para isso:
        a = f(x[i]) #aqui usariamos um if (f(x[i]))
        return myMapi(f, x, V + [a], i + 1) #se verdadeiro adiciona [a], se não:
        #faz retorno sem adicionar [a] a V

def funcao1(x):
    return x**2

funcao2 = lambda x: x**3

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y1 = myMap(funcao1, x)
y12 = myMapi(funcao1, x)

y2 = myMap(funcao2, x)
y22 = myMapi(funcao2, x)

y3 = myMapi(lambda a:a**4, x)
y32 = myMapi(lambda a:a**4, x)

print(y1)
print(y12)

print(y2)
print(y22)

print(y3)
print(y32)