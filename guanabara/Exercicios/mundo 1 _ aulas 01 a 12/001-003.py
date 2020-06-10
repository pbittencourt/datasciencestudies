# PRIMEIROS PASSOS
"""
Imprime OLÁ, MUNDO na tela -- obviamente!
Pede nome do usuário e dois números.
Exibe nome do usuário e a soma dos números inseridos
"""

print('Hello, world!!!')
nome = input('Qual é o seu nome? ')
print('Olá, {}, é um prazer te conhecer!'.format(nome))
#
idade = int(input('Qual é a sua idade? '))
print('Você tem {} anos e ano que vem você terá {} anos' .format(idade, idade + 1))

n1 = int(input('Aproveitando a brincadeira, {}, digita um número aí: ' .format(nome)))
n2 = int(input('Digita outro número, por obséquio: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}' .format(n1, n2, s))
