# MAIORES E MENORES DE IDADE

from datetime import date

print('Leremos dados de SETE pessoas! Em que ano nasceu ...')

ma = 0
me = 0
hj = date.today().year
i = []

for c in range(0, 7):
    a = int(input('... a {}a pessoa? _ ' .format(c + 1)))
    i.append(hj - a)
    if hj - a < 18:
        me += 1
    else:
        ma += 1

print('As idades são:\n{}' .format(i))
print('Temos, ao todo, {} maiores de idade e {} menores de idade.' .format(ma, me))