contaPar = 0;
contaImpar = 0;
somaPar = 0;
somaImpar = 0;
multPar = 1;
multImpar = 1;

x = int(input("Digite um numero: "));

if x%2 == 0:
	contaPar += 1; #contPar = contPar + 1
	somaPar += x; #somaPar = somaPar + x
	multPar *= x;
else:
	contaImpar += 1;
	somaImpar += x;
	multImpar *= x;

x = int(input("Digite um numero: "));

if x%2 == 0:
	contaPar += 1 ;
	somaPar += x;
	multPar *= x;
else:
	contaImpar += 1;
	somaImpar += x;
	multImpar *= x;

x = int(input("Digite um numero: "));

if x%2 == 0:
	contaPar += 1;
	somaPar += x;
	multPar *= x;
else:
	contaImpar += 1;
	somaImpar += x;
	multImpar *= x;

x = int(input("Digite um numero: "));

if x%2 == 0:
	contaPar += 1;
	somaPar += x;
	multPar *= x;
else:
	contaImpar += 1;
	somaImpar += x;
	multImpar *= x;

print(f"Foram digitados {contaPar} números pares e {contaImpar} números impares.");
print(f"Soma dos números pares: {somaPar}.");
print(f"Soma dos números impares: {somaImpar}.");

if contaPar > 0:
	print(f"Média dos números pares: {somaPar/contaPar:.2f}."); # :.2f -> para imprimir com duas casas decimais
if contaImpar > 0:
	print(f"Média dos números impares: {somaImpar/contaImpar:.2f}.");

print(f"A multiplicação dos números pares é: {multPar}.");
print(f"A multiplicação dos números impares é: {multImpar if contaImpar > 0 else 0}.");