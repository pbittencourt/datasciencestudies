# SETE VALORES, PARES OU ÍMPARES
"""O usuário digita 7 valores numéricos e cadastra-os
numa lista única, que mantem separados valores pares e ímpares.
Ao final, mostra os valores pares e ímpares em ordem crescente."""

numeros = []  # matriz para armazenar todos os valores
temp = []  # lista temporária para armazenar a cada iteração

for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: _ '))

    # resto da divisão entre n e 2
    # 0: n par
    # 1: n ímpar
    r = n % 2

    # armazena em "temp" os valores:
    # [resto, número]
    temp.append(r)
    temp.append(n)

    # copia "temp" para "numeros"
    numeros.append(temp[:])

    # limpa a lista temp p/ a próxima iteração
    temp.clear()

pares = []  # lista p/ armazenar os valores pares
impares = []  # lista p/ armazenar os valores ímpares

for num in numeros:
    # se o primeiro índice é igual a 0, o número é par
    if num[0] == 0:
        # adiciona o valor à lista dos pares
        pares.append(num[1])
    # se o primeiro índice é igual a 1, o número é ímpar
    else:
        # adiciona o valor à lista dos ímpares
        impares.append(num[1])

print(f'Os valores pares digitados foram: {sorted(pares)}.')
print(f'Os valores ímpares digitados foram: {sorted(impares)}.')
