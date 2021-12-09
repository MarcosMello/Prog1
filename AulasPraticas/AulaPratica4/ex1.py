from math import log, e, log10, sqrt, pow, log2

def main():
    x = float(input())
    f(x);

def f(x):
    if (x <= 1):
        r = log(abs(x), e)
        print(r)
    elif (x <= 2):
        r = log10(x + sqrt(x))
        print(r)
    elif (x <= 5):
        r = pow(x, 2) + pow(e, x)
        print(r)
    else:
        r = pow(x, x/2) + log2(x)
        print(r)

main();