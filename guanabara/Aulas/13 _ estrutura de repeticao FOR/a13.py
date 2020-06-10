for num in range(1, 11):
    print(num, end=' -> ')
print('fim!')

for num in range(11, 1, -1):
    print(num, end= ' -> ')
print('fim!')

print('Somente pares: ')
for p in range(0,11, 2):
    print(p, end=', ')
print('chega!')
print('Somente ímpares: ')
for i in range(1,12, 2):
    print(i, end=', ')
print('chega!')

palavra = 'pernambuco'
for letra in palavra:
    print(letra, end=', ')
print('acabou!')

frutas = ('banana', 'amora', 'morango')
for f in frutas:
    print(f'Comprei {f}!')

bebidas = ['pinga', 'cerveja', 'catuaba', 51]
for b in bebidas:
    print(f'Tomei {b}!')

pedro = {
    'idade': 32,
    'altura': 1.75,
    'qualidade': 'gostosão'
}

print('O Pedro tem:')
for att, val in enumerate(pedro):
    print(f'{att}: {val}')