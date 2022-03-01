"""
print(list(range(10)))
print(list(range(15)))
print(list(range(0, 10)))
print(list(range(5, 10)))
print(list(range(10, 15)))
print(list(range(0, 10, 2)))
print(list(range(0, 10, 3)))
print(list(range(3, 16, 3)))
"""
def myRange1(n, L = [], i = 0):
    if i == n:
        return [i] + L
    else:
        return myRange1(n, [i] + L, i+1)

def myRange2(a, b, L = []):
    if (a <= b):
        if (a == b):
            return L + [a]
        return myRange2(a + 1, b, L + [a])
    return []

def myRange3(a, b, s, L = []):
    if (a <= b):
        if (a == b):
            return L + [a]
        return myRange3(a + s, b, s, L + [a])
    return []

def myRange(a, b = None, c = None):
    return myRange1(a) if (b == c == None) else myRange2(a, b) if (c == None) else myRange3(a, b, c)

L = myRange1(10)
print(L)

L2 = myRange2(2, 10)
print(L2)

L3 = myRange3(2, 10, 2)
print(L3)

print(end = "\n\n")

LD1 = myRange(10)
LD2 = myRange(2, 10)
LD3 = myRange(2, 10, 2)
print(LD1)
print(LD2)
print(LD3)