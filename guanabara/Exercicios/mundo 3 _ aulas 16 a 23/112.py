# SEXTO EXERCÍCIO DE MÓDULOS (sextou!)
"""Criar uma função leiadinheiro(), de funcionamento simular ao input(),
mas com uma validação de dados, apenas para aceitar valores monetários.
Armazená-la no módulo utilidades.moeda"""


from utilidades import dado
from utilidades import moeda


valor = dado.leiadinheiro()
aum = dado.leiafloat('Digite um percentual de aumento: _ ')
dim = dado.leiafloat('Digite um percentual de diminuição: _ ')
moeda.resumo(valor, aum, dim)
