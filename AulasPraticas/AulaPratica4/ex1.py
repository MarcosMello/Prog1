from math import log, e, log10, sqrt, pow, log2;

x = float(input());

if (x <= 1):
    r = log(abs(x), e);
    print(r);
elif (1 < x <= 2):
    r = log10(x + sqrt(x));
    print(r);
elif (2 < x <= 5):
    r = pow(x, 2) + pow(e, x);
    print(r);
else:
    r = pow(x, x/2) + log2(x);
    print(r);