# ALISTAMENTO

from datetime import date

n = int(input('Em qual ano você nasceu? _ '))
t = date.today().year
i = t - n
m = '' if abs(18 - i) == 1 else 'm'
s = '' if abs(18 - i) == 1 else 's'

print('Você tem {} anos, então ' .format(i), end = '')

if i < 18:
    print('ainda falta{} {} ano{} para seu alistamento, que será em {}.' .format(m, 18 - i, s, n + 18))
elif i == 18:
    print('está na hora de se alistar!')
else:
    print('seu prazo de alistamento se encerrou há {} ano{}, em {}.' .format(i - 18, s, n + 18))
