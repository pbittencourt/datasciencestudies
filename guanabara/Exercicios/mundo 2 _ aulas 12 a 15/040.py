# MÉDIA ESCOLAR

n1 = float(input('Primeira nota: _ '))
n2 = float(input('Segunda nota: _ '))
m = (n1 + n2) / 2

if m < 5:
    print('Infelizmente você foi REPROVADO, pois sua média é {:.1f}' .format(m))
elif m >= 5 and m < 7: #elif 5 <= m < 7: _também funcionaria!! mlk
    print('Sua média é {} e você está de RECUPERAÇÃO' .format(m))
else:
    print('Você foi APROVADO com média {}! Parabéns!' .format(m))

# same as above
# mas com outra lógica de teste
# um pouco mais inteligente, no caso
# mandei bem! rsrsrs

if m > 7:
    print('Você foi APROVADO com média {}! Parabéns!'.format(m))
elif m >=5:
    print('Sua média é {} e você está de RECUPERAÇÃO'.format(m))
else:
    print('Infelizmente você foi REPROVADO, pois sua média é {:.1f}'.format(m))
