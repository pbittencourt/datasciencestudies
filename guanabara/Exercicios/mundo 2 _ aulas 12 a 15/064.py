# SOMANDO VÁRIOS NÚMEROS

n = i = s = 0
while n != 999:
    n = int(input('Digite um número (ou insira 999 para encerrar): _ '))
    if n != 999:
        s += n
        i += 1

print('Foram digitados {} números e a soma deles é igual a {}.'.format(i, s))
print('Fim do programa!')