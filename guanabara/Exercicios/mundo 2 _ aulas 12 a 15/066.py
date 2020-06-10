# EXIBINDO NÚMEROS ATÉ PARAR NO 999
'''O programa lê vários números inteiros, parando apenas se o usuário
digitar 999. Ao final, exibe a quantidade de valores inseridos e sua soma,
desconsiderando o 999 (flag)'''

c = s = 0       # zerando contador e soma
while True:     # equivalente ao DO (something):
    n = int(input('Insira um número (ou digite 999 para encerrar): _ '))
    if n == 999:
        break   # equivalente ao ... WHILE (condition)
    c += 1      # incrementa 1 no contador
    s += n      # acrescenta o número à soma

print(f'Foram digitados {c} números, cuja soma é {s}.')
print(f'{"FIM DO PROGRAMA":_^40}')