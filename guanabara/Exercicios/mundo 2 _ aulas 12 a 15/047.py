# SERASSI É PAR ?/

n = int(input('Kants que você quer? _ '))
for i in range(0, n + 1, 2):
    print(i, end=' ')

print('\n\nJeito alternativo:')
# consome mais processamento pq tem mais laços
for j in range(0, n + 1):
    if j % 2 == 0:
        print(j, end=' ')
