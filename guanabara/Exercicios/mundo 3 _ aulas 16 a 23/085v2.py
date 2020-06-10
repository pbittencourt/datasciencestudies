# SETE VALORES, PARES OU ÍMPARES
"""O usuário digita 7 valores numéricos e cadastra-os
numa lista única, que mantem separados valores pares e ímpares.
Ao final, mostra os valores pares e ímpares em ordem crescente."""

numeros = [[], []]  # matriz para armazenar todos os valores

for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: _ '))

    # resto da divisão entre n e 2
    # 0: n par
    # 1: n ímpar
    r = n % 2

    # adiciona 'n' na sublista 'r' de numeros
    # numeros[0] = {pares}
    # numeros[1] = {ímpares}
    numeros[r].append(n)

print(f'A lista completa ficou: {numeros}')
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')
