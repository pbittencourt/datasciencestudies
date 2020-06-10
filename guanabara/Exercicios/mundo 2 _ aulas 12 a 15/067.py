# TABUADA DE VÁRIOS NÚMEROS
'''O programa imprime a tabuada do número solicitado pelo usuário.
Ao final, pergunta se ele quer exibir a tabuada de outro valor e
assim continua, até que o usuário insira um valor negativo (flag)'''

print(f'{" TABUADÃO BOLADÃO ":=^45}')

print('Vamos exibir a tabuada (dez primeiros produtos)\ndos valores solicitados.')
print('Para encerrar, basta inserir um valor NEGATIVO.')

while True:
    print('-' * 20)
    n = int(input('Tabuada de quem? _ '))
    if n < 0:  # se digitar um valor negativo, encerra o programa
        break
    for i in range(1, 11):  # tabuada do 1 ao 10 (11 n entra no loop)
        print(f'{n} x {i:2} = {n * i}')

print('FIM DO PROGRAMA! Tenha uma boa tarde.')
