x = 2;
i = x/2;

def mod(x):
   if x > 0:
      return x;
   else:
      return x * -1;

def sqrtmine(x, i):
   if (mod(i**2 - x) < 0.000000000001):
      return i;
   else:
      i = (i+(x/i))/2;
      return sqrtmine(x, i);

print(sqrtmine(x, i));
print(2**0.5);