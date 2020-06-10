# SOMANDO APENAS OS PARES

a = []
s = 0
p = 0
for i in range(0, 6):
    n = int(input('Digite o {}o número: _ ' .format(i + 1)))
    a.append(n)
    if n % 2 == 0: # o número digitado é par
        s += n
        p += 1

print('\nVocê digitou os seguintes números:')
for i in a:
    print(i, end=' ')

print('\n\nDentre eles, {} são pares:' .format(p))
for i in a:
    if i % 2 == 0:
        print(i, end=' ')

print('\n\nA soma dos números acima mencionados é {}.' .format(s))