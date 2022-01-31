def f(m):
    if m > 0:
        f(m-1)
        print(m)

def f1(n, m):
    if n < m+1:
        print(n)
        f1(n+1, m)

f(5)
f1(5,10)