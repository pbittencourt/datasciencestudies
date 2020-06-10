# SOMA DE MULTIPLOS NUM INTERVALO

n = int(input('Até qual número cê quer? _ '))
m = int(input('Múltiplos de quem? _ '))
s = 0
c = 0

for i in range(m, n + 1, m):
    #print(i, end=', ')
    if i % 2 == 1:
        s += i
        c += 1

print('\nHá {} múltiplos ímpares de {}, entre 1 e {}, cuja soma é {}.' .format(c, m, n, s))