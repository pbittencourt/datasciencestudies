# MATRIZ 3X3
"""O programa lê 9 valores e os armazena numa matriz 3x3,
apresentando-os em seguida na forma matricial."""

matriz = [[], [], []]

for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite um valor para [{lin}, {col}]: _ ')))

print('\n A matriz final ficou assim:')
for lin in matriz:
    for col in lin:
        print(f'[ {col:^3} ]', end='')
    print('\r')
