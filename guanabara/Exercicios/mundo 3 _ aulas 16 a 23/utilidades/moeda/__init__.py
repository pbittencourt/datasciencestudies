def d(value):
    return str(value).replace('.',',')


def aumenta(valor=0, percentual=0, formatar=False):
    """
    Aumenta um valor em um certo percentual.
    :param valor: [FLOAT] o valor a ser aumentado
    :param percentual: [FLOAT] o percentual de aumento
    :param formatar: [BOOL] se o valor será formatado como moeda
    :return: [STR] o valor com o percentual aplicado
    """
    r = valor + (valor * percentual/100)
    return r if not formatar else moeda(r)


def diminui(valor=0, percentual=0, formatar=False):
    """
    Diminui um valor em um certo percentual.
    :param valor: [FLOAT] o valor a ser aumentado
    :param percentual: [FLOAT] o percentual de aumento
    :param formatar: [BOOL] se o valor será formatado como moeda
    :return: [STR] o valor com o percentual aplicado
    """
    r = valor - (valor * percentual/100)
    return r if not formatar else moeda(r)


def dobro(valor=0, formatar=False):
    r = valor * 2
    return r if not formatar else moeda(r)


def metade(valor=0, formatar=False):
    r = valor / 2
    return r if not formatar else moeda(r)


def moeda(valor=0.0, curr='R$'):
    r = f'{curr} {valor:.2f}'.replace('.', ',')
    return r


def resumo(valor=0, aum=0, dim=0):
    print('-' * 40)
    print(f'{"resumo do valor":^40}'.upper())
    print('-' * 40)

    print(f'{"Preço analisado ":.<29} ' + moeda(valor))
    print(f'{"Dobro do preço ":.<29} ' + dobro(valor, True))
    print(f'{"Metade do preço ":.<29} '+ metade(valor, True))
    aumen = d(aum) + '% de aumento '
    print(f'{aumen:.<29} ' + aumenta(valor, aum, True))
    dimin = d(dim) + '% de diminuição '
    print(f'{dimin:.<29} ' + diminui(valor, dim, True))

    print('-' * 40)
