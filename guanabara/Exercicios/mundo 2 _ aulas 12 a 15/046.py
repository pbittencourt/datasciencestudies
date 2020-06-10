# FIREWORKS

from time import sleep

print('GALERA! Vai começar! Vamos contar juntos?\n')
sleep(1)

fala = ['zero','um','dois','três',
        'quatro','cinco','seis',
        'sete','oito','nove','dez']

for i in range(10,-1,-1):
    print('{}!'.format(fala[i].capitalize()))
    sleep(1)

print('\nFELIZ ANO NOVO!')