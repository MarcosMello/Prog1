#para quando chega no numero igual (x == y), for dentro de for. 
#for (y): for (x) 
#todos com 0 = 1 e consigo mesmo também = 0
#numero com 1 = numero
#* = y!/x!(y!-x!)
"""
  0 1 2 3 4 5 6 -> x
0 1
1 1 1
2 1 2 1
3 1 3 * 1
4 1 4 * * 1
5 1 5 * * * 1
6 1 6 * * * * 1
|
V
y
"""
"""
                  1
                1   1
              1   2   1
            1   3   3   1
          1   4   6   4   1
        1   5   10  10  5   1
      1   6   15  20  15  6   1
    1   7   21  35  35  21  7   1
  1   8   28  56  70  56  28  8   1
1   9   36  84  126 126 84  36  9   1  
"""
#observacoes:
#9 * 2 espaços
#8 * 2 espaços + 1 * 3 espaços no meio

#notacao:

## n é a quantidade de linhas da piramide
## (n - (y + 1)) para espaço lateral V

##espaço no meio:

### quantidade de digitos do maior numero = V
#### se par: fazer a conta para (n, n/2) -> (y, x)
#### se impar: fazer a conta para (n, ((n+1)/2)) -> (y, x)

### num = (quantidade de digitos do maior numero) + 1 V
### (num - (quantidade de digitos do numero atual)) V