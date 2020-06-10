def nbr(value=0):
    """
    Formata um número decimal para o padrão brasileiro, utilizando vírgula para
    separar a parte inteira da parte decimal e ponto para separar classes numéricas
    :param value: o valor a ser formatado
    :return: o valor formatado
    """
    num = f'{value:,}'
    r1 = num.replace(',', ' ')
    r2 = r1.replace('.', ',')
    r = r2.replace(' ', '.')
    return r


def leiaint(value='Insira um número inteiro: _ '):
    while True:
        numero = str(input(value))
        if numero.isnumeric():
            return int(numero)
        print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
# VERSÃO ALTERNATIVA COM try ... except
# def leiaint(value='Digite um número inteiro: _ '):
#     while True:
#         try:
#             numero = int(input(value))
#         except (ValueError, TypeError):
#             print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
#         except KeyboardInterrupt:
#             print(f'\033[1;35mO usuário preferiu não digitar este valor.\033[m')
#             return 0
#         else:
#             return numero


def leiafloat(value='Insira um número: _ '):
    while True:
        entrada = str(input(value)).replace(',', '.').strip()
        if entrada.replace('.', '').isnumeric():
            return float(entrada)
        else:
            print(f'''\033[1;31mOOPS! "{entrada}" não é um número válido.\033[m''')
# VERSÃO ALTERNATIVA COM try ... except
# def leiafloat(value='Digite um número real: _ '):
#     while True:
#         texto = str(input(value)).strip().replace(',', '.')
#         try:
#             numero = float(texto)
#         except (ValueError, TypeError):
#             print(f'\033[1;31mERRO! Digite um número real válido.\033[m')
#         except KeyboardInterrupt:
#             print(f'\033[1;35mO usuário preferiu não digitar este valor.\033[m')
#             return 0
#         else:
#             return numero


def leiadinheiro(value='Insira um valor monetário: R$ '):
    while True:
        entrada = str(input(value)).replace(',', '.').strip()
        if entrada.replace('.','').isnumeric():
            return float(entrada)
        else:
            print(f'''\033[1;31mOOPS! "{entrada}" é um valor monetário inválido.\033[m''')


def leiaidade(value='Idade: _ '):
    while True:
        numero = str(input(value))
        if numero.isnumeric():
            return int(numero)
        print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')


def leianome(value='Nome: _ '):
    nome = str(input(value)).strip().title()
    return nome