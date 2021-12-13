def ehNumero(x):
    return True if (type(x) == int) else True if (isinstance(x, float)) else False

def main():
    print(ehNumero(9)) #int
    print(ehNumero(9.5)) #float
    print(ehNumero("99")) #string

main()