# INSERINDO DADOS EM UMA LISTA
"""O usuário pode adicionar vários valores numéricos em um lista, até decidir parar.
Se o dado já estiver na lista, não adiciona. Ao final, exibe todos os valores
digitados em ordem crescente"""

numeros = list()
while True:
    n = int(input('Insira um número na lista: _ '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar...')
    while True:
        c = str(input('Quer inserir outro número? [S|N]: _ ')).strip().upper()[0]
        if c in 'SN':
            break
        print('Entrada inválida!', end=' ')
    if c == 'N':
        break

print('-' * 50 + f'\nOs números digitados foram {sorted(numeros)}.')
