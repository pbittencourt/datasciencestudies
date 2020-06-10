# CADASTRÃO GERAL
"""Lê, para várias pessoas: nome, sexo, idade. Os dados de cada usuário
ficam em um dicionário e todos os dicionários ficam numa lista. Ao final:
i)   quantas pessoas foram cadastradas
ii)  a média de idade do grupo
iii) uma lista com todas as mulheres
iv)  uma lista com todas as pessoas c/ idade > média"""

# cadastro = list()  # todas as pessoas cadastradas
# pessoa = dict()  # cada registro no loop
# mulheres = list()  # listar apenas mulheres
#
# while True:
#
#     # recebe inputs do usuário
#     pessoa['nome'] = str(input('Nome: _ ')).strip().title()
#     pessoa['gênero'] = str(input('Gênero: _ ')).strip().upper()[0]
#     pessoa['idade'] = int(input('Idade: _ '))
#
#     # caso seja mulher, adiciona seu nome à lista de mulheres
#     if pessoa['gênero'] == 'F':
#         mulheres.append(pessoa['nome'])
#
#     # adiciona uma cópia de "pessoa" ao "cadastro" e
#     # limpa "pessoa" para a próxima iteração
#     cadastro.append(pessoa.copy())
#     pessoa.clear()
#
#     # verifica se o usuário quer continuar
#     opt = str(input('Quer cadastrar outro usuário? [S|N] _ ')).strip().upper()[0]
#     while True:
#         if opt in 'SN':
#             break
#         print('Entrada inválida!', end=' ')
#     if opt == 'N':
#         break
#
# fim do loop principal

# apenas para teste (s/ precisar dos inputs chatos...)
cadastro = [
    {'nome': 'Pedro', 'gênero': 'M', 'idade': 32},
    {'nome': 'Paloma', 'gênero': 'F', 'idade': 22},
    {'nome': 'Jonas', 'gênero': 'M', 'idade': 17},
    {'nome': 'Andressa', 'gênero': 'F', 'idade': 28},
    {'nome': 'Gabriel', 'gênero': 'M', 'idade': 56},
    {'nome': 'Maitê', 'gênero': 'F', 'idade': 47},
    {'nome': 'Zara', 'gênero': 'F', 'idade': 8}
]
mulheres = list()
for m in range(0, len(cadastro)):
    if cadastro[m]['gênero'] == 'F':
        mulheres.append(cadastro[m]['nome'])
# fim do bloco de testes (comentar na versão final)

# total de pessoas cadastradas
total = len(cadastro)

# cálculo da idade média das pessoas
somaidade = 0
for i in range(0, total):
    somaidade += cadastro[i]['idade']
idademedia = somaidade / total

# lista pessoas acima da média do grupo
acimamedia = list()
for i in range(0, total):
    if cadastro[i]['idade'] > idademedia:
        acimamedia.append(cadastro[i]['nome'])

# exibe os resultados
print(f'A) Foram cadastradas {total} pessoas.')
print(f'B) A idade média do grupo é {idademedia:.1f} anos.')
print(f'C) As mulheres do grupo são: {mulheres}.')
print(f'D) As pessoas acima da média de idade do grupo são: {acimamedia}')
