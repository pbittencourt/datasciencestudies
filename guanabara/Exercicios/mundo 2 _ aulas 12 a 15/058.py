# JOGO DE ADIVINHAÇÃO v2.0

from random import randint
from time import sleep

m = 10
c = randint(1, m)
p = str(input('Qual é o seu nome? ')).title()
print('=*=.' * 13)
print('HELLO, {}. I WANNA PLAY A GAME!'.format(p.upper()))
print('Escolhi um número entre 1 e {}.\nTente adivinhar em qual número eu estou pensando... ' .format(m))
print('=*=.' * 13)

acertou = False
n = 0   # palpite do jogador
r = w = 0   # right and wrong answers! :)
while not acertou:
    n = int(input('Seu palpite (pressione 0 para sair): _ '))
    sleep(0.5)
    if n == 0:
        break
    print('AGUARDE... estou processando...')
    sleep(1)

    if n == c:
        print('PARABÉNS! Você acertou!!!')
        r += 1
        acertou = True
    else:
        print('ERROU! Tente ',end='')
        w += 1
        if n < c:
            print('subir um pouco...')
        else:
            print('descer um pouco...')
print('=*=.' * 13)
print('FIM DO JOGO!\nPlacar final: ', end='')
if w > r:
    print('COMPUTADOR {} X {} {}' . format(w, r, p.upper()))
else:
    print('{} {} x {} COMPUTADOR'.format(p.upper(), r, w))
