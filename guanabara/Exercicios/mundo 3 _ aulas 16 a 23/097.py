# ESCRITA ADAPTADA
"""Uma função escreve um texto bonitinho, com linhas acima
e abaixo, de forma a acompanhar o tamanho da mensagem"""


def escreva(txt, sym = '~', opt = 'title'):
    tam = len(txt) + 2
    print(sym * tam)
    if opt == 'title':
        print(f' {txt} '.title())
    elif opt == 'capitalize':
        print(f' {txt} '.capitalize())
    elif opt == 'upper':
        print(f' {txt} '.upper())
    else:
        print(f' {txt} ')
    print(sym * tam)


escreva('pedro bittencourt')
escreva('rapaz, que coisa mais doida!', sym = '=')
escreva('aprendendo python 3+', opt='upper')
