# MATRIZ 3X3 APRIMORADO
"""O programa lê 9 valores e os armazena numa matriz 3x3,
apresentando-os em seguida na forma matricial. Ao final, mostra:
i)   A soma de todos os valores pares digitados
ii)  A soma dos valores da terceira coluna
iii) O maior valor da segunda linha"""

matriz = [[], [], []]

# loop para armazenar dados na matriz
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um valor para [{lin}, {col}]: _ ')))

# inicializa algumas variáveis:
# soma_pares: soma dos valores pares
# soma_col2 = soma dos valores da 3a coluna
# maior_lin1 = maior valor da 2a linha
soma_pares = soma_col2 = maior_lin1 = 0

print('\nA matriz completa ficou:\n')

# loop para exibir a matriz e obter informações a seu respeito
# i: índice da linha
# j: índice da coluna
for i, lin in enumerate(matriz):
    for j, col in enumerate(lin):
        print(f'[ {col:^3} ]', end='')

        # se o número é par, some-o com 'soma_pares'
        if col % 2 == 0:
            soma_pares += col

        # se estivermos na 3a coluna (j == 2),
        # some o número a 'soma_col2':
        if j == 2:
            soma_col2 += col

        # verifica se o valor é o maior
        # da 2a linha (i == 1):
        if i == 1:
            if col > maior_lin1:
                maior_lin1 = col
    print('\r')

print(f'\nA soma de todos os valores pares digitados é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_col2}.')
print(f'O maior valor da segunda linha é {maior_lin1}.')
