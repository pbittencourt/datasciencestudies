# NATAÇÃO MANO

from datetime import date

a = int(input('Seu ano de nascimento: _ '))
i = date.today().year - a

print('Você tem {} anos, então será alocado para a categoria' .format(i), end = ' ')

if i > 20:
    print('MASTER.')
elif i > 19:
    print('SÊNIOR.')
elif i > 14:
    print('JÚNIOR.')
elif i > 9:
    print('INFANTIL.')
else:
    print('MIRIM.')
