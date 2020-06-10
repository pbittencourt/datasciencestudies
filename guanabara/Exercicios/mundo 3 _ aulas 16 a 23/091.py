# SORTEIO DOS DADOS
"""O programa gera aleatoriamente os resultados de 4 jogadores
que lançaram dados. Feito isto, armazena as jogadas num dicionário.
Em seguida, coloca-as em ordem crescente, mostrando o ranking"""

from random import randint
from time import sleep
from operator import itemgetter

jogos = dict()
print(f'{"OS DADOS FORAM LANÇADOS!":<33}')
print('=' * 33)
sleep(1)
for i in range(1, 5):
    jogador = f'jogador{i}'
    jogada = randint(1, 6)
    jogos[jogador] = jogada
    print(f'\tO jogador \"{jogador}\" tirou {jogada}!')
    sleep(0.5)

print(f'\n{"RANKING DOS JOGADORES:":<33}')
print('=' * 33)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
# print(ranking)
for k, v in enumerate(ranking):
    print(f'\t{k + 1}º lugar: Jogador \"{v[0]}\", que tirou {v[1]} no dado.')
    sleep(0.5)
