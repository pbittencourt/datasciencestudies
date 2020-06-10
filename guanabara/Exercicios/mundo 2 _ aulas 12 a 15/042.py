# REFAZENDO EX035

from time import sleep

cor = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m',
    'branco_vermelho': '\033[30;41m',
    'branco_verde': '\033[30;42m',
    'branco_amarelo': '\033[30;43m',
    'branco_azul': '\033[30;44m',
    'branco_magenta': '\033[30;45m',
    'branco_ciano': '\033[30;46m',
    'branco_cinza': '\033[30;47m',
}

a = float(input('{}Primeira aresta:{} _ ' .format(cor['branco_amarelo'], cor['limpa'])))
b = float(input('{}Segunda aresta:{} _ ' .format(cor['branco_magenta'], cor['limpa'])))
c = float(input('{}Terceira aresta:{} _ ' .format(cor['branco_azul'], cor['limpa'])))

if a == b == c: # same as 'a == b and b == c'
    t = 'equilátero'
elif a == b or a == c:
    t = 'isósceles'
else:
    t = 'escaleno'

print('\n{} ANALISANDO... {}\n' .format(cor['branco_ciano'], cor['limpa']))
sleep(1)

if a < (b + c) and a > abs(b - c):
    print('{}É POSSÍVEL{} formar um triângulo {}{}{} de lados {:.2f}, {:.2f} e {:.2f}!' .format(cor['verde'], cor['limpa'], cor['branco_cinza'], t, cor['limpa'], a, b, c,))
else:
    print('{}NÃO É POSSÍVEL{} formar um triângulo de lados {:.2f}, {:.2f} e {:.2f}!' .format(cor['vermelho'], cor['limpa'], a, b, c))

print('Compare o maior lado com a soma dos menores:')

lado = [int(a), int(b), int(c)]
lado.sort()

"""print(lado)
corlado = {
    int(a): cor['amarelo'],
    int(b): cor['magenta'],
    int(c): cor['azul']
}
print(corlado)
corlado.sort()
print(corlado)"""

print('{}=' .format(cor['azul']) * lado[2])
print('{}=' .format(cor['amarelo']) * lado[1], end = '')
print('{}=' .format(cor['magenta']) * lado[0])
