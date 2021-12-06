""" #E1 -> Erro = name 'mensagemRepetida' is not defined
mensagemRepetida()

#Define , mas nao executa , a funcao mensagem
def mensagem():
    print("Minha função feita em Python.")
    print("Esse é um exemplo de função sem parâmetro e sem retorno.")

#Define , mas nao executa , a funcao mensagemRepetida
def mensagemRepetida():
    mensagem()
    mensagem()

#Chama (executa) a funcao mensagemRepetida
"""

#""" #E2 -> Roda normalmente
#Define , mas nao executa , a funcao mensagemRepetida
def mensagemRepetida():
    mensagem()
    mensagem()

#Define , mas nao executa , a funcao mensagem
def mensagem():
    print("Minha função feita em Python.")
    print("Esse é um exemplo de função sem parâmetro e sem retorno.")

#Chama (executa) a funcao mensagemRepetida
mensagemRepetida()
#"""