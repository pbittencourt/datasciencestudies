# TERCEIRO EXERCÍCIO DE MÓDULOS
"""Modificação para que as funções do ex107 aceitem
um parâmetro a mais, informando se o valor retornado será
ou não formatado pela função moeda(), desenvolvida no ex108"""


from ex109 import moeda


valor = float(input('Digite um valor: R$ '))
aum = float(input('Digite um percentual de aumento: _ '))
dim = float(input('Digite um percentual de diminuição: _ '))
print(f'{moeda.moeda(valor)}, aumentado de {aum} % é {moeda.aumenta(valor, aum, True)}.')
print(f'{moeda.moeda(valor)}, diminuido de {dim} % é {moeda.diminui(valor, dim, True)}.')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}.')
