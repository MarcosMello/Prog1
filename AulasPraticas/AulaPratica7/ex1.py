def f1(n, m): #printar de n até m | depois de modificar: printa de n até m e depois de m até n
    if n <= m:
        print("Ida: ", n)
        f1(n + 1, m)
        print("Volta: ", n)

def f2(n, m): #printar de n até m
    if n > m:
        return # mesmo que return None
    else:
        print(n)
        f2(n + 1, m)

def f3(n, m): #printar de n até m
    print(n)
    if n == m:
        return None 
    f3(n + 1, m)

def f4(n, m): #printar de n até m
    print(n)
    if n != m:
        f4(n + 1, m)

def f5(n, m): #printar de m até n
    if n <= m:
        f5(n + 1, m)
        print(n)

def main():
    print("f1(0, 10)")
    f1(10, 0)
    print("f2(0, 10)")
    f2(10, 0)
    # print("f3(0, 10)")
    # f3(10, 0) #REC INF - ==
    # print("f4(0, 10)")
    # f4(10, 0) #REC INF - != 
    print("f5(0, 10)")
    f5(10, 0)

main()