# LENDO INTEIROS E FLOATS COM EXCEÇÕES
"""Reescrever função leiaint() do exercício 104 e criar
função leiafloat(), utilizando, dessa vez, tratamento a exceções."""


def leiaint(value='Digite um número inteiro: _ '):
    while True:
        try:
            numero = int(input(value))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;35mO usuário preferiu não digitar este valor.\033[m')
            return 0
        else:
            return numero


def leiafloat(value='Digite um número real: _ '):
    while True:
        texto = str(input(value)).strip().replace(',', '.')
        try:
            numero = float(texto)
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;35mO usuário preferiu não digitar este valor.\033[m')
            return 0
        else:
            return numero


i = leiaint()
r = leiafloat()
print(f'Digitastes o número inteiro {i} e o número real {r:.2f}')
