# CONDICOES DE EXISTENCIA DE TRIANGULOOOOS

from time import sleep

a = float(input('\033[31mPrimeira aresta: _ '))
b = float(input('\033[34mSegunda aresta: _ '))
c = float(input('\033[36mTerceira aresta: _ '))

print('\n\033[1;35mAnalisando...')
sleep(3)

if a < (b + c) and a > abs(b - c):
    print('\033[1;32mÉ POSSÍVEL formar um triângulo de lados {}, {} e {}!' .format(a, b, c))
else:
    print('\033[1;33mNÃO É POSSÍVEL formar um triângulo de lados {}, {} e {}!' .format(a, b, c))

print('\033[0;37mObserve:')
print('\033[31m=' * int(a))
print('\033[34m=' * int(b))
print('\033[36m=' * int(c))
