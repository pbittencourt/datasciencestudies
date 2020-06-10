# PRIMEIRO EXERCÍCIO DE MÓDULOS
"""Criar um módulo chamado moeda.py, contendo as funções
aumentar(), diminuir(), dobro() e metade(). O programa em
questão importa esse módulo e utiliza algumas de suas funções."""

from ex107 import moeda

valor = float(input('Digite um valor: R$ '))
aum = float(input('Digite um percentual de aumento: _ '))
dim = float(input('Digite um percentual de diminuição: _ '))
print(f'R$ {valor}, aumentado de {aum} % é R$ {moeda.aumenta(valor, aum)}.')
print(f'R$ {valor}, diminuido de {dim} % é R$ {moeda.diminui(valor, dim)}.')
print(f'O dobro de R$ {valor} é R$ {moeda.dobro(valor)}.')
print(f'A metade de R$ {valor} é R$ {moeda.metade(valor)}.')
