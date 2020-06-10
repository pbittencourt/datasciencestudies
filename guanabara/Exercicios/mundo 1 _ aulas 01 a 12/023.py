num = input('Insira um número de 0 a 9999: ')

print('Do meu jeito convencional de sempre:')

j = 0
k = len(num) - 1
pos = ['unidades', 'dezenas', 'centenas', 'unidades de milhar']
print('O número digitado possui: ')
while j < len(num):
    print('{} {}'.format(num[k], pos[j]))
    j += 1
    k -= 1

print('=' * 30)

print('Agora, utilizando uma nova estratégia:')

n = int(num)
u = n // 1 % 10  # divisao inteira, modulo
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Unidades de milhar: {}'.format(m))

print('=' * 30)

print('Same as above, but with LOOPS!')

j = 0
while j < len(num):
    char = n // (10 ** j) % 10
    print('{} {}' .format(char, pos[j]))
    j += 1

print('\nTHE END!')
