# JOGO DE ADIVINHAÇÃO

from random import randint
from time import sleep

c = randint(0, 5)
p = str(input('Qual é o seu nome? '))
print('=*=.' * 10)
print('\nHELLO, {}. I WANNA PLAY A GAME!\n'.format(p.upper()))

print('Escolhi um número entre 0 e 5.')
n = int(input('Tente adivinhar em qual número eu estou pensando... : '))
sleep(1)
print('AGUARDE... estou processando...')
sleep(2)

if n == c:
    print('PARABÉNS! Você acertou!!!')
else:
    print('Poxa, não foi dessa vez... eu escolhi o número {}!' .format(c))
