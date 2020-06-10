# LISTA DE COMPRAS
"""Lê o nome e o preço de vários produtos, perguntando
se o usuário quer continuar. Ao final, mostra:
i)   total da compra
ii)  quantos produtos custam +R$ 1k
iii) nome do produto mais barato"""

qtd = 0             # quantidade de itens
total = 0           # total da compra
acima_mil = 0       # qtd de itens +R$1k
preco_barato = 0    # preço do +barato
nome_barato = ''    # nome do item +barato

while True:
    qtd += 1

    print('-' * 40)
    titulo = f'Registro do {qtd}º produto'.upper()
    print(f'{titulo:^40}')
    print('-' * 40)

    # pega nome e preço do produto
    nome = str(input(f'Digite o nome do {qtd}º produto: _ ')).strip().capitalize()
    preco = float(input(f'Digite o preço do {qtd}º produto: R$ '))

    # total da compra
    total += preco

    # verifica se o preço foi +R$ 1k
    if preco > 1000:
        acima_mil += 1

    # verifica se eh o +barato
    # (na 1a iteração smp será!)
    if qtd == 1 or preco < preco_barato:
        preco_barato = preco
        nome_barato = nome

    continuar = ' '  # isso ainda é um hack né ... :(
    while continuar not in 'sSnN':
        continuar = str(input('Registrar outro produto? [S|N] _ ')).strip().upper()[0]
    if continuar in 'nN':
        break  # o usuário encerrou o programa

print('=' * 40)
print('Registro finalizado com sucesso!')
print(f'Foram registrados {qtd} produtos, num total de \033[30;45mR$ {total:8.2f}\033[m.')
# na linha acima, {total:8.2f} significa exibir 8 digitos, inclusos ja os 2 decimais
# tipo o que acontece no SQL !
print(f'Dentre eles, {acima_mil} têm preço superior a R$ 1000.00.')
print(f'\033[4;36m{nome_barato}\033[m é o produto mais barato da lista, custando apenas R$ {preco_barato:.2f}.')
print('=' * 40 + '\nTenha um bom dia e volte sempre!')
