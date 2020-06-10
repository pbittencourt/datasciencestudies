# PALPITES MEGASENA
"""O programa pergunta quantos jogos serão gerados,
sorteando 6 números entre 1 e 60 para cada jogo,
cadastrando tudo numa única lista composta."""

from random import randint
from time import sleep

# cabeçalho bonitinho!
print('=' * 40 + f'\n{"Jogando na Mega Sena":^40}\n'.upper() + '='* 40)

n = int(input('Quantos jogos você quer que eu sorteie? '))
jogo = list()  # um jogo individual
jogos = list()  # todos os jogos gerados

print(f'Estou sorteando {n} jogos, aguarde ...')
sleep(2)

# loop para gerar todos os jogos (n escolhas)
for i in range(0, n):

    # loop para gerar cada jogo individual (seis números)
    for j in range(0, 6):

        # verifica se o número sorteado já pertence à lista deste jogo
        while True:
            # sorteia um número entre 1 e 60
            n = randint(1, 60)

            # se n estiver em jogo, retorna ao início do loop.
            # em caso contrário, quebra o loop e carrega o
            # número sorteado p/ o próximo bloco
            if n not in jogo:
                break

        # adiciona o número sorteado ao jogo atual
        jogo.append(n)

    # mostra o jogo gerado
    print(f'Jogo nº {i + 1}: {sorted(jogo)}')

    # copia o jogo p/ a lista com todos os jogos
    jogos.append(sorted(jogo[:]))

    # limpa a variável de jogo individual p/ a próxima iteração
    jogo.clear()

    sleep(1.5)

print('-' * 40 + '\nProcesso finalizado!\nBoa sorte (:')
