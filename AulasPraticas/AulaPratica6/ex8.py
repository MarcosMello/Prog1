from os import system, name  #Funções usadas para limpar a tela do terminal

def limpaTela(): 
	"""
	Função responsável por limpar o terminal. 
	Para isso, a função precisa saber o Sistema Operacional (SO) que o código está sendo executado.
	A definição do nome do SO é feito com auxílio do módulo 'os'. Supõem-se que o código
	será executado em Windows ou Linux. Se estiver usando outro SO, leia a documentação do 
	módulo 'os' para fazer as modificações necessárias. 
	Para saber mais: https://docs.python.org/pt-br/3.8/library/os.html
	"""
	if name == 'nt':  #Windows
		system('cls') 
	else:  #Linux ou outro SO
		system('clear') 

def telaAbertura():
	"""
	Função responsável por exibir uma "tela" de boas-vindas aos usuários
	"""
	RST     = '\033[00m'
	RED     = '\033[31m'
	BLUE    = '\033[34m'
	print(BLUE) #Muda a cor da fonte para azul
	print("######                                                    ")
	print("#     # ###### #    #       #    # # #    # #####   ####  ")
	print("#     # #      ##  ##       #    # # ##   # #    # #    # ")
	print("######  #####  # ## # ##### #    # # # #  # #    # #    # ")
	print("#     # #      #    #       #    # # #  # # #    # #    # ")
	print("#     # #      #    #        #  #  # #   ## #    # #    # ")
	print("######  ###### #    #         ##   # #    # #####   ####  ") 
	print()
	print(RED) #Muda a cor da fonte para vermelho
	_ = input("--> Enter para continuar...")
	print(RST) #Reseta a cor

def menu():
	"""
	Função responsável por exibir as opções disponíveis ao usuário
	"""
	RST     = '\033[00m'
	BLUE    = '\033[34m'
	print(BLUE) #Muda a cor da fonte para azul
	print("+" + "-"*50 + "+")
	print("|" + " "*50 + "|")
	print("|    SISTEMA DE CALCULO DE CUSTO DE COMBUSTÍVEL    |")
	print("|" + " "*50 + "|")
	print("+" + "-"*50 + "+")
	print("|" + " "*50 + "|")
	print("| 1 - Vitoria................................230km |")
	print("| 2 - Rio de Janeiro.........................750km |")
	print("| 3 - São Paulo.............................1200km |")
	print("| 4 - Recife................................1700km |")
	print("| 5 - Florianópolis.........................1900km |")
	print("|" + " "*50 + "|")
	print("+" + "-"*50 + "+")
	print(RST) #Reseta a cor
	

def escolheDestino(n):
	"""
	Retorna o número do destino escolhido

	Parâmentro:
	n: quantidade de destinos
	"""
	x = int(input("--> Escolha o seu destino: "))

	if x < 1 or x > 5:
		print("Destino inválido! Você deve digitar um valor entre 1 e 5.")
		return escolheDestino(n)
	else:
		return x

def imprimeCusto(destino, consumo, precoCombustivel):
	"""
	Função responsável por calcular e imprimir o custo da viagem de acordo com os
	dados passados como parâmetro.

	Por simplicidade a função considera que o 'destino' é um valor válido (entre 1 e 5). 
	Em um programa real, devemos tratar o caso de o 'destivo' ser inválido.
	"""
	RST     = '\033[00m'
	GREEN   = "\033[1;32m" #Fonte verde e em negrito

	if destino == 1:
		distancia = 230
		cidade = "Vitória"
	elif destino == 2:
		distancia = 750
		cidade = "Rio de Janeiro"
	elif destino == 3:
		distancia = 1200
		cidade = "São Paulo"
	elif destino == 4:
		distancia = 1700
		cidade = "Recife"
	elif destino == 5:
		distancia = 1900
		cidade = "Florianópolis"

	custo = (distancia/consumo)*precoCombustivel
	print(f"\n{GREEN}O custo da viagem até {cidade} será de R${custo:.2f}{RST}")


def programa(i = 1):
	"""
	Função responsável pelo gerenciamos do programa. 
	"""
	RST     = '\033[00m'
	YELLOW  = '\033[33m'

	limpaTela()
	menu()

	destino = escolheDestino(5)
	consumo = float(input("Digite o consumo (km/l) do seu carro: "))
	precoCombustivel = float(input("Digite o preço do combustível: "))
	
	imprimeCusto(destino, consumo, precoCombustivel)

	print(YELLOW)
	resp = input("Deseja fazer o cálculo para outro destino (S/N)? ")
	print(RST)
	if resp == "S" or resp == "s":
		programa(i + 1)
	else:
		print(f"Finalizando o programa após {i} execuç{'ões' if i > 1 else 'ão'}") #Note a utilização de expressão ternária

def main():
	"""
	Função main tradicional. 
	"""
	limpaTela()    #Limpa a tela do terminal
	telaAbertura() #Exibe a tela de abertura quando o programa é executado
	programa()     #Inicia a execução do programa
	print("FIM!!!")

main()

#Exemplos de cores que podem ser usadas no terminal:
# GRAY    = '\033[30m'
# RED     = '\033[31m'
# GREEN   = '\033[32m'
# YELLOW  = '\033[33m'
# BLUE    = '\033[34m'
# VIOLET  = '\033[35m'
# CYAN    = '\033[36m'
# WHITE   = '\033[37m'
#Veja mais exemplos em: https://gist.github.com/vratiu/9780109