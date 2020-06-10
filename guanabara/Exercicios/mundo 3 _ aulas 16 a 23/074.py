# NUMEROS EM UMA TUPLA
"""O programa sorteia cinco números aleatórios e armazena-os em uma tupla.
Após isso, mostra a listagem de numeros gerados indicando o maior e o menor valor"""

from random import randint

# trapaceando no exercício.
# só que depois eu tive uma ideia.
# no segundo bloco do programa vc confere!
numeros = []
for i in range(0, 5):
    numeros.append(randint(1, 10))

print('Os números sorteados foram: ', end='')
for i in numeros:
    print(i, end=' ')

print(f'\n\nO menor valor sorteado foi: {sorted(numeros)[0]}.')
print(f'O maior valor sorteado foi: {sorted(numeros)[-1]}.')

####################################################################

print('\n' + '=' * 50)
print('TIVE UMA IDEIA!\n')

numeros = str(randint(10000,99999))
print('Os números sorteados foram: ', end='')
for i in range(0, 5):
    print(numeros[i], end=' ')

print(f'\n\nO menor valor sorteado foi: {sorted(numeros)[0]}.')
print(f'O maior valor sorteado foi: {sorted(numeros)[-1]}.')

####################################################################

print('\n' + '=' * 50)
print('Sugestão da usuária Roberta Schmitz no youtube:')

from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
