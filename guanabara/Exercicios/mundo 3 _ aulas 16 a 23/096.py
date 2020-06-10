# ÁREA DE UM TERRENO
"""Pega as dimensões de um terreno retangular e retorna a medida de sua área"""


def area(l, c):
    print(f'A área de um terreno retangular de dimensões {l:.1f} m e {c:.1f} m é {l * c:.2f} m².')


def titulo(txt):
    tam = len(txt) + 2
    print('~' * tam)
    print(f' {txt} '.upper())
    print('~' * tam)


titulo('Controle de terrenos')

largura = float(input('Largura (m): _ '))
comprimento = float(input('Comprimento (m): _ '))

area(largura, comprimento)
