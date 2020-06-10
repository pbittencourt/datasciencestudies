# PROGRESSÃO ARITMÉTICA com while
fim = False
while fim == False:
    print('=' * 44)
    print('{:^44}'.format(' PROGRESSÃO ARITMÉTICA '))
    print('{:^44}'.format('Exibindo os dez primeiros termos de uma PA'))
    print('=' * 44)

    a1 = int(input('Primeiro termo: _ '))
    r = int(input('Razão: _ '))
    c = 1
    an = a1
    while c <= 10:
        print(an, end=' > ')
        an += r
        c += 1

    print('fim')
    opt = str(input('\nDeseja reiniciar o programa? [S|N] _ ')).strip().upper()[0]
    fim = True if opt == 'N' else False

print('\nPrograma encerrado. Tenha um bom dia!')