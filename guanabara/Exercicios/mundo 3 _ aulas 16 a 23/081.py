# COLOCANDO NÚMEROS NA LISTA E FORNECENDO INFOS
"""O programa lê vários números (enquanto o usuário quiser) e
armazena-os numa lista. Ao final, exibe:
i)   Quantos números foram digitados
ii)  A lista em ordem decrescente
iii) Se existe um 5, quantas vezes e onde aparece"""

valores = []
while True:
    valores.append(int(input('Digite um valor: _ ')))

    while True:
        opt = str(input('Deseja continuar? [S|N] _ ')).strip().upper()[0]
        if opt in 'SN':
            break
        else:
            print('Entrada inválida!', end=' ')
    if opt == 'N':
        break

plurais = ('i', 'ram', 'o', 'os', 'r', 'res')
plu = []
if len(valores) == 1:
    # pegarei os índices pares
    plu = [plurais[0], plurais[2], plurais[4]]
else:
    # pegarei os índices ímpares
    plu = [plurais[1], plurais[3], plurais[5]]

print('\n' + '_'*7 + f'\nFo{plu[0]} digitad{plu[1]} {len(valores)} valo{plu[2]}. Em ordem de inserção: {valores}.')

if valores.count(5) > 0:
    plu1 = 'es' if valores.count(5) > 1 else ''
    plu2 = 's' if valores.count(5) > 1 else ''
    plu3 = 'ões' if valores.count(5) > 1 else 'ão'
    pos = list()
    for j, n in enumerate(valores):
        if n == 5:
            pos.append(j)
    print(f'O valor 5 faz parte da lista. Ele foi digitado {valores.count(5)} vez{plu1}, na{plu2} posiç{plu3} {pos}')
else:
    print('O valor 5 não faz parte da lista.')

print(f'A lista, em ordem decrescente, ficou: {sorted(valores, reverse=True)}.')
