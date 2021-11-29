""" #Exercicio 1
nota1 = 7.0;
nota2 = 8.2;
nota3 = 6.5;

print("Nota da primeira prova:", nota1);
print("Nota da segunda prova:", nota2);
print("Nota da terceira prova:", nota3);

media = (nota1 + nota2 + nota3)/3

print("Nota Media do Aluno:", media);
print("Prova final? ", media < 7);
"""

""" #Exercicio 2
pi = 3.14;

r = float(input("Insira o raio: "));

v = (4/3) * pi * r**3;
a = 4 * pi * r**2;

print("Para um raio " + str(r) + ", o volume é", v, "e a area é", a, ".");
"""

#""" #Exercicio 3 - v1 -> Mais Preciso
segr = seg = int(input("Digite os segundos: "));

horas = segr // 3600;
segr -= horas * 3600;

minutos = segr // 60;
segr -= minutos * 60;

segundos = segr;

print(horas, ":", minutos, ":", segundos);
#"""

""" #Exercicio 3 - v2 -> Menos Preciso
seg = int(input("Digite os segundos: "));

horas = seg / 3600;
minutos = ((horas - int(horas)) * 3600) / 60);
segundos = ((minutos - int(minutos)) * 60);

print(int(horas), ":", int(minutos), ":", int(segundos));
"""