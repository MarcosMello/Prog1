"""def f(n, x = 0):
    if n == 2:
        return x + 2
    elif n % 2 == 0:
        x += n;
    
    return f(n-1, x)

def f1(n):
    if n == 2:
        return 2
    elif n % 2 == 1:
        return f(n-1)
    else:
        return n + f(n-1)

print(f(10))
print(f1(10))"""

a = 1
t = 1
f = 1
ar = 1


print(True if (a and t and f and ar) else False)