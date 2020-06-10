# LISTAS COM PARES E ÍMPARES
"""Lê vários valores (até o user interromper o laço) e os armazena numa lista.
Ao final, analista a lista gerada e gera outras duas: uma com os valores pares
e outra com os valores ímpares digitados."""

lista = list()
while True:
    lista.append(int(input('Digite um valor: _ ')))
    while True:
        opt = str(input('Quer continuar? [S|N] _ ')).strip().upper()[0]
        if opt in 'SN':
            break
        else:
            print('Entrada inválida!', end=' ')
    if opt == 'N':
        break

pares = list()
impares = list()

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('_' * 20 + f'\nLista completa: {lista}.')
print(f'Lista de pares: {pares}.')
print(f'Lista de ímpares: {impares}.')
