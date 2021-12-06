def main():
    s = int(input("Digite a quatidade de segundos: "));
    converte(s);

def converte(segundos):
    horas = segundos//3600;
    segundos -= horas*3600;

    minutos = segundos//60;
    segundos -= minutos*60;

    print(f"{horas} : {minutos} : {segundos}");

main();