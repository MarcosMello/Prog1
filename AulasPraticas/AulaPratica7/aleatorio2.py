import random as r
import math

def simulacaoV1(escolha, n):
	"""
	Faz n jogadas de um dado e retorna a quantidade de acertos do jogador

	Parâmetros:
	escolha: número inteiro entre 1 e 6, escolhido pelo jogador
	n: número de vezes que um dado será jogado

	Returno:
	Número de vezes que "escolha" foi sorteado
	"""
	#Valida os parâmestros
	if type(escolha) != int or type(n) != int or not (1 <= escolha <= 6) or n < 0:
		print("Erro: valores inválidos")
		return 0
	elif n == 0: # Verifica se foram feitos os n sorteios
		return 0
	else: # Ainda deve ser feito sorteios
		x = r.randint(1, 6) #Faz o sorteio
		if x == escolha:
			return 1 + simulacaoV1(escolha, n - 1)
		else:
			return simulacaoV1(escolha, n - 1)

def simulacaoV2(escolha, n, i = 0, acertos = 0):
	"""
	Faz n jogadas de um dado e retorna a quantidade e a média de acertos do jogador

	Parâmetros:
	escolha: número inteiro entre 1 e 6, escolhido pelo jogador
	n: número de vezes que um dado será jogado

	Returno:
	Número de vezes que "escolha" foi sorteado e a média de acertos
	"""
	#Valida os parâmestros
	if type(escolha) != int or type(n) != int or not (1 <= escolha <= 6) or n <= 0:
		print("Erro: valores inválidos")
		return 0, 0
	elif i == n: # Verifica se foram feitos os n sorteios
		return acertos, acertos / n #Retorna o número de acertos e a média dos acertos
	else: # Ainda deve ser feito sorteios
		x = r.randint(1, 6) #Faz o sorteio
		if x == escolha: 
			return simulacaoV2(escolha, n, i + 1, acertos +1)
		else:
			return simulacaoV2(escolha, n, i + 1, acertos)

def imprime(v, jogadas):
	a, m = simulacaoV2(v, jogadas)
	print(jogadas, a, m)

def main():
	v = int(input("Digite o valor apostado entre 1 e 6: "))
	print(10, simulacaoV1(v, 10))
	print(50, simulacaoV1(v, 50))
	print(100, simulacaoV1(v, 100))
	print(250, simulacaoV1(v, 250))
	print(500, simulacaoV1(v, 500))
	print()
	imprime(v, 10)
	imprime(v, 50)
	imprime(v, 100)
	imprime(v, 250)
	imprime(v, 500)
	
main()

#Sim, algumas vezes mais proximo do que outras.