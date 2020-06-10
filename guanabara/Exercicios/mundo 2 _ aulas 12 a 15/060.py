# TRABALHANDO COM FATORIAIS!!!!! <<<<

print('{:=^40}'.format(' [ CALCULADORA DE FATORIAIS ] '))
n = int(input('Insira um número: _ '))
print('-' * 40)

print('O fatorial de {} é {}! = ' .format(n, n), end='')
i = n
f = 1
while i > 0:
    print('{}'.format(i), end=' ')
    print('x' if i != 1 else '=',end=' ')
    f *= i
    i -= 1
print('{}\n'.format(f))
print('=' * 40)

print('\nSAME AS ABOVE, mas com FOR:')
g = 1
print('O fatorial de {} é {}! = ' .format(n, n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end=' ')
    print('x' if c != 1 else '=', end=' ')
    g *= c
print('{}'.format(g))
