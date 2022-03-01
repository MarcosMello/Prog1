def uniao(l1, l2):
    return semRepetidos(l1+l2)

def semRepetidos(lr, lf = [], i = 0):
    if (i < len(lr)):
        if (lr[i] not in lf):
            return semRepetidos(lr, lf + [lr[i]], i + 1)
        else:
            return semRepetidos(lr, lf, i + 1)
    return lf

print(uniao([1,2,3,3], [1, 5, 3]))