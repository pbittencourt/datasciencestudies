# SIMULADOR DE CAIXA ELETRÔNICO
"""O usuário insere o valor em R$ que pretende sacar.
A partir disto, o programa deve calcular quantas cédulas
de cada valor serão entregues, considerando que o caixa
possui cédulas de 50, 20, 10 e 1"""

from time import sleep  # só pra fazer uma graça

print('$' * 50)
print('{:^50}'.format(' BANKOSTENTAÇÃO '))
print('{:^50}'.format('Aqui o seu dinheiro rende mais!'))
print('$' * 50, end='\n\n')

valor = int(input('Quer sacar quanto? _ R$ '))

saque = 0       # valor do saque em R$ -- no começo, nada!
cedulas = 0     # quantidade de células sacadas -- no começo, tb nada!!
resto = valor   # quanto ainda resta para sacar? no começo, tudo!!!

i = 0                   # índice para rodar a lista de valores das cédulas
ced = [50, 20, 10, 1]   # lista com os valores das cédulas

while resto != 0:  # enquanto tiver dinheiro a ser sacado, continue

    # resto da divisão inteira do valor a ser sacado ("atual resto") pela atual cédula do índice
    cedulas = resto // ced[i]

    # se houver cédulas a serem exibidas, continua!
    if cedulas != 0:
        singular = '' if cedulas == 1 else 's'  # teste para exibir cédulA ou cédulAS
        print(f'Retirando {cedulas} cédula{singular} de R$ {ced[i]:.2f} ... ')
        sleep(1)  # faz um suspensinho .... rsrsrs

    # acrescenta ao saque a quantidade em R$ que foi retirada nessa iteração
    saque += ced[i] * cedulas

    # atribui ao atual resto o quanto ainda falta para a próxima cédula
    resto = resto % ced[i]

    # rola o índice para o próximo valor de cédula!
    i += 1

print('_' * 50)
print('Operação finalizada. Tenha um bom dia!')
