def f(x, y = 1):
    if (x == y):
        return x
    elif (x % y == 0):
        return y + f(x, y+1)
    else:
        return f(x, y+1)

def ehPerfeito(x, f = f):
    if (x >= 0):
        if ((f(x) - x) == x):
            return True
        else:
            return False
    else:
        return None

def perfeitos(q, c = 1, f = ehPerfeito):
    if (c == q):
        print(f"O numero {c}{'é' if f(c) else 'não é'} perfeito.")
    else:
        print(f"O numero {c} {'é' if f(c) else 'não é'} perfeito.")

        c += 1

        return perfeitos(q, c)

def main():
    num = int(input())
    perfeitos(num)

main()