import random as r

def main():
	print(r.random()) #Gera um número aleatório entre [0, 1), ou seja, 0.0 <= x < 1.0

	print(r.uniform(2.5, 10.0)) #Gera um número aleatório entre [2.5, 10], ou seja,  2.5 <= x < 10.0

	print(r.randrange(10))        # Gera um número inteiro entre [0, 9], ou seja, 0 <= x <= 9
	print(r.randrange(0, 101, 2)) # Gera um número inteiro *par* entre [0, 100], ou seja, 0 <= x <= 100 e x % 2 == 0

	print(r.randint(1, 6))        #Sorteia um número inteiro entre [1, 6]

main()

#Não foram os mesmos