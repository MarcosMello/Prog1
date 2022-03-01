def semRepetidos(lr, lf = [], i = 0):
    if (i < len(lr)):
        if (lr[i] not in lf):
            return semRepetidos(lr, lf + [lr[i]], i + 1)
        else:
            return semRepetidos(lr, lf, i + 1)
    return lf

print(semRepetidos([1, 2, 1, 3, 2, 1, 4, 0]))