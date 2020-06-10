# colorize me!

cln = '\033[m'  # cor 'limpa'
cor = {
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m',
    'branco_vermelho': '\033[30;41m',
    'branco_verde': '\033[30;42m',
    'branco_amarelo': '\033[30;43m',
    'branco_azul': '\033[30;44m',
    'branco_magenta': '\033[30;45m',
    'branco_ciano': '\033[30;46m',
    'branco_cinza': '\033[30;47m',
}

for i in cor:
    print(f'{cor[i]}{i}{cln}')
