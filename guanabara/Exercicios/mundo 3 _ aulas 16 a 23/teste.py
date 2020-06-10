# Testando coisas


def fuckme(value):
    num = f'{value:,}'
    r1 = num.replace(',', ' ')
    r2 = r1.replace('.', ',')
    r = r2.replace(' ', '.')
    return r


def fn(valor=0, cla='.', dec=','):
    # separa as partes inteira e decimal, se for o caso
    parte = str(valor).split('.')

    # a parte inteira fica pro primeiro elemento da lista
    inteira = parte[0]

    # inicia o loop de separação da parte inteira em classes numéricas
    cont = 1
    saida = ''
    while cont <= len(inteira):
        numero = inteira[-cont:]
        digito = inteira[-cont]
        digitos = len(numero)
        if digitos % 3 == 1 and digitos != 1:
            saida += cla
        saida += digito
        cont += 1

    # se houver parte decimal, ela fica pro segundo elemento da lista
    # neste caso, exiba-a
    if len(parte) > 1:
        r = saida[::-1] + dec + parte[1]
    else:
        r = saida[::-1]

    return r


a = 123
print(fn(a))
b = 12345
print(fn(b))
c = 12345.6
print(fn(c))
d = 9999999999
print(fn(d))

print(fuckme(123456.78))
