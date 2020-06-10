# SÓ DEIXA PASSAR NÚMERO
"""Criar uma função leiaInt() que só deixa passar valor inteiro.
Em caso negativo, retorna mensagem de erro até o usuário digitar
um valor permitido."""


def leiaint(value='Digite um número: _ '):
    while True:
        numero = str(input(value))
        if numero.isnumeric():
            return int(numero)
        print(f'\033[41mERRO! Digite um número inteiro válido.\033[m')


n = leiaint()
print(f'Você acabou de digitar o número {n}.')
print(f'O resto da divisão de {n} por 2 é {n % 2}.')
