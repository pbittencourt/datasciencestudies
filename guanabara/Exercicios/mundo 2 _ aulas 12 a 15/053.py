# PALINDROMOSSSS

f = str(input('Digite uma frase: _ ')).strip().upper().replace(' ', '')
r = ''
for i in range(len(f), 0, -1):
    r += f[i - 1]
# o laço acima poderia ser subst por
# r = f[::-1]

print('Sua frase original, sem espaços, é:\n{}'.format(f))
print('Sua frase, revertida, ficou:\n{}'.format(r))
print('Conclui-se, portanto, que essa frase', end=' ')
print('\033[1;30;44m É \033[m' if f == r else '\033[1;30;41m NÃO É \033[m', end=' um palíndromo!')
