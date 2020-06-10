# QUARTO EXERCÍCIO DE MÓDULOS
"""Aprimora os exercícios anteriores, adicionando a
função resumo(), que mostra na tela algumas informações
geradas pelas funções que já temos até então"""


from ex110 import moeda


valor = float(input('Digite um valor: R$ '))
aum = float(input('Digite um percentual de aumento: _ '))
dim = float(input('Digite um percentual de diminuição: _ '))
moeda.resumo(valor, aum, dim)
