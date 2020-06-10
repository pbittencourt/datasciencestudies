# FATORIAL


def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    Permite a exibição do processo de cálculo.
    :param num: número a ser determinado o fatorial
    :param show: se as etapas do cálculo serão exibidas
    :return: o fatorial de num
    """
    fator = 1
    texto = ''
    for n in range(num, 0, -1):
        fator *= n
        if show:
            sep = ' x ' if n != 1 else ' = '
            texto += repr(n) + sep
    texto += repr(fator)
    return texto


numero = int(input('Digite um número para ter seu fatorial determinado: _ '))
exibir = str(input('Quer exibir o cálculo completo? [S|N] _ ')).strip().upper()[0]
opcao = True if exibir == 'S' else False

print(f'{numero}! = {fatorial(numero, opcao)}')
help(fatorial)
