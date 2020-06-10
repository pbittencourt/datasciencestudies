# LISTAGEM DE PREÇOS
"""Uma tupla armazena nomes e preços de produtos, de forma sequencial.
Após isto, exibe-os numa listagem tabular, similar a comprovante de compra"""

compra = (
    'Pinga', 9.5,
    'Cerveja', 22.4,
    'catuaba', 11.9,
    'Água de côco', 15,
    'Amendoim', 8.99,
    'Camisinha', 12.99,
    'Lubrificante', 22.40,
)

l = ('-', 60)

# cabeçalho da listagem
print(l[0]*l[1] + f'\n{"listagem de preços":^60}\n'.upper() + l[0]*l[1])

# i: índice do item | item: item em si (dã!)
for i, item in enumerate(compra):

    if i % 2 == 0:
        # se o índice é par, temos o nome do item
        print(f'{item.capitalize():.<50}', end='')
    else:
        # se o índice é ímpar, temos o preço do item
        print(f' R$ {item:6.2f}')

print(l[0]*l[1])