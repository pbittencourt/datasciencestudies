# SERASSI EH PRIMO

n = int(input('Digite um número: _ '))
d = []
for i in range (1, n + 1):
    if n % i == 0:
        d.append(i)

print('O número {} tem {} divisores:\n{}' .format(n, len(d), d))
print('Conclui-se, portanto, que o número {}' .format(n), end=' ')
print('\033[1;30;44m É \033[m' if len(d) == 2 else '\033[1;30;41m NÃO É \033[m', end=' primo.')