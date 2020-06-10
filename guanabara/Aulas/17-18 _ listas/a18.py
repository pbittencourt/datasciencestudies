# CONTINUANDO COM AS LIXTAIX....
# to sum up: listas dentro de listas

pessoas = list()  # armazenaremos várias pessoas aqui!
pedro = ['Pedro', 32]
paloma = ['Paloma', 22]
fulano = ['José', 25]
pessoas.append(pedro)
pessoas.append(paloma)
pessoas.append(fulano[:])  # cópia de fulano
print(pessoas)

# modificando fulano
fulano[0] = 'Maria'
fulano[1] = 33
pessoas.append(fulano[:])  # cópia de fulano
print(pessoas)

print(pessoas[0])
print(pessoas[1][0])
print(pessoas[2][1])

for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos.')

galera = list()
pessoa = list()
for i in range(0, 3):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Idade: ')))
    galera.append(pessoa[:])
    pessoa.clear()
print(galera)
