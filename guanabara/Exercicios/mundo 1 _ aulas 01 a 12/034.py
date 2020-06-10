# AUMENTO DE SALÁRIOOO!!!

s = float(input('Digite seu salário: R$ '))

if s <= 1250:
    i = 0.15
else:
    i = 0.1

print('Você recebeu um aumento de {}%!' .format(int(i * 100)))
print('Seu novo salário é de R$ {:.2f}.' .format(s * (1+i)))