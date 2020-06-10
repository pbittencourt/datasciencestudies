# SISTEMA INTERATIVO DE AJUDA
"""Mini sistema que utiliza o interactive help do Python:
o usuário digita um comando e aparece o manuel. Ao digitar
'fim' o programa é encerrado."""


from time import sleep


cor = {
    'limpa': '\033[m',
    'vermelho': '\033[30;41m',
    'verde': '\033[30;42m',
    'amarelo': '\033[30;43m',
    'azul': '\033[30;44m',
    'magenta': '\033[30;45m',
    'ciano': '\033[30;46m',
    'cinza': '\033[30;47m',
}


def titulo(value):
    tamanho = len(value) + 4
    print('\n' + f'{cor["magenta"]}~' * tamanho + f'{cor["limpa"]}')
    print(f'{cor["magenta"]}  {value}  {cor["limpa"]}')
    print(f'{cor["magenta"]}~' * tamanho + f'{cor["limpa"]}\n')


def ajudaluciano(value):
    sleep(0.3)
    titulo(f'Acessando o manual do comando \"{value.upper()}\"')
    sleep(1)
    print(cor['azul'])
    help(value)
    print(cor['limpa'])


while True:
    ajuda = str(input(f'Função ou biblioteca: _ ').strip())
    if ajuda.lower() == 'fim':
        sleep(1)
        print(f'{cor["cinza"]}CABÔ O PROGRAMA! Simone, encerra o programa aí! Chega, cab-{cor["limpa"]}')
        break
    ajudaluciano(ajuda)
