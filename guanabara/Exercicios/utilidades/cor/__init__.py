c = {'z': '\033[m'}
l = ['w', 'r', 'g', 'y', 'b', 'm', 'c', 'k']

i = j = 0
for lin in range(30, 38):
    c[l[i]] = f'\033[{lin}m'
    i += 1

i = j = 0
for lin in range(30, 38):
    for col in range(40, 48):
        c[l[i] + l[j]] = f'\033[{lin};{col}m'
        j += 1
    i += 1
    j = 0


def clr(text='', value='z'):
    return c[value] + str(text) + c['z']
