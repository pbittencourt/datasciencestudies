# Introdução às "f" strings
# (interpolação dentro de strings)
# só delícia, irmão!!!

nome = 'Pedro'
idade = 32
salario = 1500.328
print('-' * 50)
print('PYTHON 2:')
print('O %s tem %d anos.' % (nome, idade))
print('PYTHON ~3.5:')
print('O {} tem {} anos.'.format(nome, idade))
print('PYTHON 3.6+:')
print(f'O {nome.upper():_^20} tem {idade} anos e recebe R$ {salario:.2f} por mês.')