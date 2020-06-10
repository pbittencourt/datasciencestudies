# DISSECANDO UMA VARIÁVEL
"""
O programa lê algo inserido pelo usuário e retorna
algumas informações sobre o tipo primitivo da variável.
"""

var = input('Digite algo: _ ')
print('O valor digitado tem, como tipo primitivo:', type(var))
print('Só tem espaços?', var.isspace())
print('É um número?', var.isnumeric())
print('É alfabético?', var.isalpha())
print('É alfanumérico?', var.isalnum())
print('Está em maiúsculas?', var.isupper())
print('Está em minúsculas?', var.islower())
print('Está capitalizada?', var.istitle())
