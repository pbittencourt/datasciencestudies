# MÓDULO DO EXERCÍCIO 109


def aumenta(valor=0, percentual=0, formatar=False):
    """
    Aumenta um valor em um certo percentual.
    :param valor: [FLOAT] o valor a ser aumentado
    :param percentual: [FLOAT] o percentual de aumento
    :param formatar: [BOOL] se o valor será formatado como moeda
    :return: [STR] o valor com o percentual aplicado
    """
    r = valor + (valor * percentual/100)
    return r if formatar is False else moeda(r)


def diminui(valor=0, percentual=0, formatar=False):
    """
    Diminui um valor em um certo percentual.
    :param valor: [FLOAT] o valor a ser aumentado
    :param percentual: [FLOAT] o percentual de aumento
    :param formatar: [BOOL] se o valor será formatado como moeda
    :return: [STR] o valor com o percentual aplicado
    """
    r = valor - (valor * percentual/100)
    return r if not formatar else moeda(r)  # same as function above returns!


def dobro(valor=0, formatar=False):
    r = valor * 2
    return r if formatar is False else moeda(r)


def metade(valor=0, formatar=False):
    r = valor / 2
    return r if formatar is False else moeda(r)


def moeda(valor=0.0, curr='R$'):
    r = f'{curr} {valor:.2f}'.replace('.', ',')
    return r
