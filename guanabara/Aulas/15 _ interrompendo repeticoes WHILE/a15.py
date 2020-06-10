# CONTINUANDO COM ESTUDOS DE LAÇOS
# do ... while
# PLUS: introdução às "f" strings
# (interpolação dentro de strings)
# só delícia, irmão!!!

cont = 1
while True:
    if cont > 10:
        break
    print(cont, ' > ', end='')
    cont += 1
print('FIM!')

c = s = 0
a = []
while True:
    n = int(input('Digite um número (ou 999 para encerrar): _ '))
    if n == 999:
        break
    s += n
    c += 1
    a.append(n)
#print('Foram digitados {} números e sua soma é {}.'.format(c, s))
print(f'Foram digitados {c} números e sua soma é {s}.')
