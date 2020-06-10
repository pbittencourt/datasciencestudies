# QUAL É O PREÇO DA PASSAGEM?

d = float(input('Qual é a distância da viagem, em km? _ '))

if d <= 200:
    i = 0.50
    print('Essa é uma viagem curta!')
else:
    i = 0.45
    print('Essa é uma viagem longa!')

print('Cobraremos R$ {:.2f} por cada km rodado.'.format(i))
print('O preço final da passagem é R$ {:.2f}.'.format(d * i))
print('Obrigado por comprar com VACILO ROADS!')