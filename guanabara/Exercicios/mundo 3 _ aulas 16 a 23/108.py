# SEGUNDO EXERCÍCIO DE MÓDULOS
"""Aprimorar o exercício 107, adicionando formatação de moedas."""

from ex108 import moeda

valor = float(input('Digite um valor: R$ '))
aum = float(input('Digite um percentual de aumento: _ '))
dim = float(input('Digite um percentual de diminuição: _ '))
print(f'{moeda.moeda(valor)}, aumentado de {aum} % é {moeda.moeda(moeda.aumenta(valor, aum))}.')
print(f'{moeda.moeda(valor)}, diminuido de {dim} % é {moeda.moeda(moeda.diminui(valor, dim))}.')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}.')
