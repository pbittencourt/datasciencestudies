# QUER PAGAR QUANTO?

print('{:=^40}' .format(' QUER PAGAR QUANTO? '))

c = float(input('Kants que custa? R$ '))
print('''Escolha a forma de pagamento:
1) à vista no dinheiro ou cheque;
2) à vista no cartão;
3) 2x no cartão;
4) 3x ou mais no cartão.''')
f = int(input('Forma de pagamento: _ '))

if f == 1:
    print('Você pagará R$ {:.2f}.' .format(0.9 * c))
elif f == 2:
    print('Você pagará R$ {:.2f}.' .format(0.95 * c))
elif f == 3:
    print('Você pagará R$ {:.2f}, em duas parcelas de R$ {:.2f}.'.format(c, c / 2))
elif f == 4:
    p = int(input('Quantas parcelas? _ '))
    print('Você pagará R$ {:.2f}, em {} parcelas de R$ {:.2f}.'.format(1.2 * c, p, (1.2 * c) / p))
else:
    print('Opção inválida! Tente novamente.')

print('\n{:*^40}'.format(' Tenha um bom dia! '))