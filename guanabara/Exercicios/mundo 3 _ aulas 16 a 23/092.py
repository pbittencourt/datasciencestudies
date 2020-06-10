# CADASTRO DE FUNCIONÁRIO

"""Lê nome, ano de nascimento e carteira de trabalho de um funcionário
e cadastra-os, com idade, em um dicionário. Se por acaso a CTPS for
diferente de zero, o dicionário tb recebe o ano de contratação e o
salário. Calcular e acrescentar, além da idade, com quantos
anos a pessoa vai se aposentar (RISOS VÍDEO DE 2017 rsrsrs)..."""

from datetime import date

# recebe inputs do usuário
nome = str(input('Nome: _ ')).strip().title()
ano = int(input('Ano de nascimento: _ '))
ctps = int(input('CTPS (0 não tem): _ '))

# armazena informações no dict funcionário{}
funcionario = {
    'nome': nome,
    'idade': date.today().year - ano,
    'ctps': ctps
}

# se houver CTPS, pede mais informações
if ctps != 0:
    funcionario['contratacao'] = int(input('Ano de contratação: _ '))
    funcionario['salario'] = float(input('Salário: R$ '))
    # aposentadoria = 35 anos a mais da idade em que começou a trabalhar
    # (obtida a partir da diferença entre anos de contratação e nascimento)
    funcionario['aposentadoria'] = 35 + funcionario['contratacao'] - ano

# exibe informações do usuário na forma de dicionário
print(funcionario)

# exibe informações do usuário na forma sequencial
for k, v in funcionario.items():
    print(f'{k} tem valor {v}')
