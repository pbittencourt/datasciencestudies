# MAIOR E MENOR DENTRE CINCO
"""Lê cinco números e mostra maior e menor, além da(s)
posição(ões) em que apareceram na lista"""

numeros = list()
for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a {i + 1}ª posição: _ ')))

print(f'Você digitou os valores {numeros}.')
print(f'O maior valor digitado foi {max(numeros)} na(s) posição(ões): ', end='')
for i in range(0, len(numeros)):
    if numeros[i] == max(numeros):
        print(i + 1, end='... ')
print(f'\nO menor valor digitado foi {min(numeros)} na(s) posição(ões): ', end='')
for i in range(0, len(numeros)):
    if numeros[i] == min(numeros):
        print(i + 1, end='... ')
