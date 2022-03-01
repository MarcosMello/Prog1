import random

def myRange(a, b, L = []):
    if (a <= b):
        if (a == b):
            return L + [a]
        return myRange(a + 1, b, L + [a])
    return []

def sorteioMegaSena(i = 0, L = []):
    if (i < 6):
        num = random.choice(myRange(1, 60))

        if (num not in L):
            return sorteioMegaSena(i + 1, L + [num])
        return sorteioMegaSena(i, L)

    return L

print(sorteioMegaSena())