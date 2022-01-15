def fibb (n, c = 1, n1 = 1, n2 = 1):
    if (n == 0):
        print(f"0")
    elif (n > 0):
        if (c == n):
            print(n1 + n2)
        else:
            if (c == 1 or c == 2):
                print(1)
                return fibb(n, c + 1, n1, n2)
            else:
                s = n1 + n2
                print(s)

                return fibb(n, c + 1, n2, s)       
    else:
        print(f"Erro!")
        return None

fibb(12)