# QUINTO EXERCÍCIO DE MÓDULOS
"""Cria um pacote chamado 'utilidades', dentro do qual serão armazenados
os módulos 'dado' e 'moeda'. Transferir para este segundo as funções
até então desenvolvidas e manter o programa funcionando."""


from utilidades import moeda

valor = float(input('Digite um valor: R$ '))
aum = float(input('Digite um percentual de aumento: _ '))
dim = float(input('Digite um percentual de diminuição: _ '))
moeda.resumo(valor, aum, dim)
