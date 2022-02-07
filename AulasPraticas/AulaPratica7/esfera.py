from math import pi 

def areaEsfera1():
	"""
	Função que faz a leitura do raio de uma esfera e imprime sua área

	Argumentos:
		Nenhum
	Return:
		Nada
	Exemplo:
        >>> areEsfera1()
        Digite o raio da esfera: 10
        Area: 1256.6370614359173
	"""
	r = float(input("Digite o raio da esfera: "))
	print("Area: {}".format(4*pi*r**2))

def areaEsfera2(r):
	"""
	Função que recebe o raio de uma esfera e imprime sua área
	
	Argumentos:
		r (float): raio da esfera
	Return:
		Nada
	Exemplo:
        >>> areEsfera2(10)
        Area: 1256.6370614359173
	"""
	print("Area: {}".format(4*pi*r**2))

def areaEsfera3(r):
	"""
	Função que recebe o raio de uma esfera e retorna sua área
	
	Argumentos:
		r (float): raio da esfera
	Return:
		A área da esfera de raio r
	Exemplo:
        >>> areEsfera3(10)
		1256.6370614359173
	
    Obs.: Perceba que essa função não possui nenhum print. Por isso, ao ser
          utilizada em um script o valor retornado deve ser armazenado em 
          uma variável (para ser utilizados posteriormente) ou impresso.   
	"""
	return 4*pi*r**2

