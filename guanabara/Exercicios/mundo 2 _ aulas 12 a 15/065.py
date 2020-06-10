# MÉDIA INFITINTAAAA

opt = 'S'               # opção inicial SIM
c = s = ma = me = 0     # zerando contador, soma, maior e menor

while opt in 'sS':
    n = float(input('Digite um número: _ '))
    c += 1
    s += n

    if c == 1 or n < me:  # 1o laço OU n é menor
        me = n
    if n > ma:
        ma = n

    opt = str(input('Você quer inserir outro valor? [S|N] _ ')).strip().upper()

print('-' * 30)
print('Você inseriu {} valores que, somados, resultam em {:.1f},\nPortanto, a média é igual a {:.2f}.'.format(c, s, (s/c)))
print('O maior valor digitado foi {:.1f} e o menor foi {:.1f}.'.format(ma, me))
