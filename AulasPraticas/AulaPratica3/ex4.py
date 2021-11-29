n = int(input("Digite um número: "));

if 100 <= n <= 999:
    if 100 <= n < 200:
        n -= 100;
        n1 = 1;
    elif 200 <= n < 300:
        n -= 200;
        n1 = 2;
    elif 300 <= n < 400:
        n -= 300;
        n1 = 3;
    elif 400 <= n < 500:
        n -= 400;
        n1 = 4;
    elif 500 <= n < 600:
        n -= 500;
        n1 = 5;
    elif 600 <= n < 700:
        n -= 600;
        n1 = 6;
    elif 700 <= n < 800:
        n -= 700;
        n1 = 7;
    elif 800 <= n < 900:
        n -= 800;
        n1 = 8;
    else:
        n -= 900;
        n1 = 9;

    if 10 <= n < 20:
        n -= 10;
        n2 = 1;
        n3 = n;
    elif 20 <= n < 30:
        n -= 20;
        n2 = 2;
        n3 = n;
    elif 30 <= n < 40:
        n -= 30;
        n2 = 3;
        n3 = n;
    elif 40 <= n < 50:
        n -= 40;
        n2 = 4;
        n3 = n;
    elif 50 <= n < 60:
        n -= 50;
        n2 = 5;
        n3 = n;
    elif 60 <= n < 70:
        n -= 60;
        n2 = 6;
        n3 = n;
    elif 70 <= n < 80:
        n -= 70;
        n2 = 7;
        n3 = n;
    elif 80 <= n < 90:
        n -= 80;
        n2 = 8;
        n3 = n;
    else:
        n -= 90;
        n2 = 9;
        n3 = n;
    
    if (n1 < n2 < n3):
        print(f"{(n1*100)+(n2*10)+n3} é ascendente. (n1 = {n1}, n2 = {n2}, n3 = {n3})");
    else:
        print(f"{(n1*100)+(n2*10)+n3} não é ascendente. (n1 = {n1}, n2 = {n2}, n3 = {n3})");
else:
    print("ERRO");