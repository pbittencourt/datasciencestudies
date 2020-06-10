# MÓDULO DO EXERCÍCIO 108


def aumenta(m=0, p=0):
    r = m + (m * p/100)
    return r


def diminui(m=0, p=0):
    r = m - (m * p/100)
    return r


def dobro(m=0):
    r = m * 2
    return r


def metade(m=0):
    r = m / 2
    return r


def moeda(m=0, c='R$'):
    r = f'{c} {m:.2f}'.replace('.', ',')
    return r
