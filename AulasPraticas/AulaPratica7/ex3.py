def b(n): #imprime os numeros em binario
    if n != 0:
        return n % 2 + 10 * b(n // 2)
    
    return 0

print(b(1))
print(b(2))
print(b(3))
print(b(4))
print(b(5))
print(b(6))
print(b(7))
print(b(8))
print(b(9))
print(b(10))