import math

""" #E1

x1 = int(input());
y1 = int(input());
x2 = int(input());
y2 = int(input());

d = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2));
print(d);

"""

#""" #E2

a = int(input());
b = int(input());
c = int(input());

delta = math.pow(b, 2) - 4 * a * c;

if delta >= 0:

    x1 = (- b + math.sqrt(delta))/(2*a);
    x2 = (- b - math.sqrt(delta))/(2*a);

    if x1 != x2:
        print(x1);
        print(x2);
    else:
        print(x1);

else:
    print("ERRO!");

#"""