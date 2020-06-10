def leiadinheiro(value='Insira um valor monetário: R$ '):
    while True:
        entrada = str(input(value)).replace(',', '.').strip()
        if entrada.replace('.','').isnumeric():
            return float(entrada)
        else:
            print(f'''\033[1;31mOOPS! "{entrada}" é um preço inválido.\033[m''')


def leiaint(value='Insira um número inteiro: _ '):
    while True:
        numero = str(input(value))
        if numero.isnumeric():
            return int(numero)
        print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')


def leiafloat(value='Insira um número: _ '):
    while True:
        entrada = str(input(value)).replace(',', '.').strip()
        if entrada.replace('.', '').isnumeric():
            return float(entrada)
        else:
            print(f'''\033[1;31mOOPS! "{entrada}" não é um número válido.\033[m''')


def d(value):
    return str(value).replace('.',',')