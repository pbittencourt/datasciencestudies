# QUAL É O MAIOR NÚMERO?

a = int(input('Insira o primeiro número: _ '))
b = int(input('Insira o segundo número: _ '))
c = int(input('Insira o terceiro número: _ '))

me = a # definindo, a principio, a como MEnor
if b <a and b < c:
    me = b # então MEnor recebe b
if c < a and c < b:
    me = c # então MEnor recebe c
ma = a #definindo, a principio, a como MAior
if b > a and b > c:
    ma = b # então MAior recebe b
if c > a and c > b:
    ma = c # então MAior recebe c

print('O maior valor digitado foi {} e, o menor, {}.' .format(ma, me))

print('=' * 20)
print('Isso também poderia ser feito com listas...')
lista = [a, b, c]
lista.sort()
print('O maior valor digitado foi {} e, o menor, {}.' .format(lista[len(lista)-1], lista[0]))
