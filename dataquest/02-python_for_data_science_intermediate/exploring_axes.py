# APRENDENDO A UTILIZAR EIXOS NO NUMPY

import numpy as np


def titulo(texto=''):
    print('-' * 40)
    print(texto.upper().center(40))
    print('-' * 40)


##########################
# MATRIZES DE 1 DIMENSÃO #
##########################

titulo('uma dimensão')

one_dimensional = np.array([1, 1, 2, 3, 5])
print('Matriz:\n', one_dimensional)
sum_one_dimensional = one_dimensional.sum(0)
print('Soma dos elementos (axis=None):', sum_one_dimensional)

# retorna o mesmo resultado:
sum_one_dimensional = one_dimensional.sum(axis=0)
print('Soma dos elementos (axis=0):', sum_one_dimensional)

# retorna erro:
# sum_one_dimensional = one_dimensional.sum(axis=1)
# print(sum_one_dimensional)
# >>> numpy.AxisError: axis 1 is out of bounds for array of dimension 1

###########################
# MATRIZES DE 2 DIMENSÕES #
###########################

titulo('duas dimensões')

two_dimensional = np.array(
    [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
)
print('Matriz:\n', two_dimensional)

# soma todos os elementos da matriz:
sum_two_dimensional = two_dimensional.sum()
print('Soma de todos os elementos da matriz (axis=None):', sum_two_dimensional)

# soma os elementos das colunas
sum_two_dimensional = two_dimensional.sum(0)
print('Soma dos elementos das colunas (axis=0):', sum_two_dimensional)

# soma os elementos das linhas:
sum_two_dimensional = two_dimensional.sum(1)
print('Soma dos elementos das linhas (axis=1):', sum_two_dimensional)

# retorna erro
# sum_two_dimensional = two_dimensional.sum(2)
# print(sum_two_dimensional)
# >>> numpy.AxisError: axis 2 is out of bounds for array of dimension 2

###########################
# MATRIZES DE 3 DIMENSÕES #
###########################

titulo('três dimensões')

three_dimensional = np.array(
    [
        [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ],
        [
            [9, 10, 11],
            [12, 13, 14],
            [15, 16, 17]
        ]
    ]
)
print('Matriz:\n', three_dimensional)

# soma todos os elementos da matriz
sum_three_dimensional = three_dimensional.sum()
print('\nSoma de todos os elementos da matriz (axis=None):', sum_three_dimensional)

# soma "de cima para baixo"
sum_three_dimensional = three_dimensional.sum(0)
print('''\nSoma "de cima para baixo" (axis=0):\n''', sum_three_dimensional)

# soma "de frente para o fundo"
sum_three_dimensional = three_dimensional.sum(1)
print('''\nSoma "de frente para o fundo" (axis=1):\n''', sum_three_dimensional)

# soma "da esquerda para a direita"
sum_three_dimensional = three_dimensional.sum(2)
print('''\nSoma "da esquerda para a direita" (axis=2):\n''', sum_three_dimensional)

# retorna erro
# sum_three_dimensional = three_dimensional.sum(3)
# print(sum_three_dimensional)
# >>> numpy.AxisError: axis 3 is out of bounds for array of dimension 3
