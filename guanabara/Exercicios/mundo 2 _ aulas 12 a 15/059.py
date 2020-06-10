# ESCOLHA A OPERAÇÃO!

from time import sleep

opt = 0 # zerando as opções

while opt != 5: # a opção 5 encerra o loop
    # se o programa começou agora ou se o usuário pedir por novos números:
    if opt == 0 or opt == 4:
        n1 = float(input('Insira o primeiro número: _ '))
        n2 = float(input('Insira o segundo número: _ '))

    opt = int(input('''O que você deseja fazer com os números {:.1f} e {:.1f}?
    [1] somar
    [2] multiplicar
    [3] descobrir o maior
    [4] inserir novos números
    [5] encerrar o programa
Opção escolhida: _ ''' .format(n1, n2)))

    print('=' * 30)
    if opt == 1:
        print('Aguarde um instante ...')
        sleep(1)
        print('A soma entre {:.1f} e {:.1f} é {:.1f}'.format(n1, n2, n1 + n2))
        print('=' * 30)
    elif opt == 2:
        print('Aguarde um instante ...')
        sleep(1)
        print('O produto de {:.1f} com {:.1f} é {:.1f}'.format(n1, n2, n1 * n2))
        print('=' * 30)
    elif opt == 3:
        print('Aguarde um instante ...')
        sleep(1)
        print('O maior valor entre {:.1f} e {:.1f} é'.format(n1, n2), end='')
        if n1 > n2:
            print(' {:.1f}'.format(n1))
        elif n2 > n1:
            print(' {:.1f}'.format(n2))
        else:
            print(', na verdade, nenhum deles, pois ambos são iguais!')
        print('=' * 30)
    elif opt == 4:
        print('Inserindo novos números ...')
    elif opt == 5:
        print('Encerrando ...')
        print('=' * 30)
    else:
        print('Opção inválida! Tente novamente.')
    sleep(1)

print('Fim do programa. Tenha um bom dia!')
