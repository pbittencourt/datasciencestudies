# JO KEN PÔ!

from random import randint
from time import sleep

cor = {
    'limpa': '\033[m',
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

print('{:-^30}' .format(' [ JO KEN PÔ! ] '))

print('''Vamos brincar? Escolha uma das opções abaixo:
1) Pedra
2) Papel
3) Tesoura''')
o = ['', 'pedra', 'papel', 'tesoura']
p = int(input('\nSua escolha: _ '))

c = randint(1, 3)

if p == c:
    w = 'deu empate!'
elif p == 1:
    if c == 3:
        w = 'você é o vencedor!'
    else:
        w = 'eu sou o vencedor!'
elif p == 2:
    if c == 1:
        w = 'você é o vencedor!'
    else:
        w = 'eu sou o vencedor!'
elif p == 3:
    if c == 2:
        w = 'você é o vencedor!'
    else:
        w = 'eu sou o vencedor!'
else:
    print('Opção inválida!')
    exit()

print('\nWAIT FOR IT ...\n')
sleep(1)
print('{} JO {}' .format(cor['branco_vermelho'], cor['limpa']))
sleep(0.5)
print('{} KEN {}' .format(cor['branco_verde'], cor['limpa']))
sleep(0.5)
print('{} PO! {}\n' .format(cor['branco_azul'], cor['limpa']))

print('Eu escolhi {}{}{} \ne você escolheu {}{}{}. \nSendo assim, {}{}{}'.format(cor['magenta'], o[c], cor['limpa'], cor['amarelo'], o[p], cor['limpa'], cor['branco_ciano'], w, cor['limpa']))
