# DICIONÁRIOS

sep = '-' * 30

fulano = {
    'nome': 'Abel',
    'idade': 33,
    'altura': 1.85
}

print(fulano)
print(fulano['nome'])
print(fulano['idade'])
print(fulano['altura'])
print(f'O {fulano["nome"]} tem {fulano["idade"]} anos.')

print(sep)

print(fulano.keys())
print(fulano.values())
print(fulano.items())

print(sep)

for k in fulano.keys():
    print(f'Chave {k}')
for v in fulano.values():
    print(f'Valor {v}')
for i in fulano.items():
    print(f'Item {i}')
for k, v in fulano.items():  # parecido com enumerate
    print(f'Chave {k} com valor {v}')

print(sep)

del fulano['idade']
print(fulano)

fulano['nome'] = 'Pedro'  # altera s/ problemas!
print(fulano)

fulano['altura'] = 1.75  # ñ precisa dar append()
fulano['peso'] = 60.5
print(fulano)

print(sep)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[1])
print(brasil[0]['sigla'])

print(sep)

pessoa = {
    'nome': 'Pedro',
    'idade': 32,
    'altura': 1.74,
    'qualidades': [
        'lindo', 'tesão', 'bonito', 'gostosão'
    ]
}

for k, v in pessoa.items():
    print(f'O {k} é {v}.')
    print(type(k))
    print(type(v))

print(sep)

# brasil = list()
# estado = dict()
# for i in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: _ '))
#     estado['sigla'] = str(input('Sigla do estado: _ '))
#     # brasil.append(estado) __ vai copiar 3x o último registro (cópia emaranhada!)
#     # brasil.append(estado[:] __ fatiamento não funciona em dicionários
#     brasil.append(estado.copy())
# print(brasil)
brasil = [
    {'uf': 'Acre', 'sigla': 'AC'},
    {'uf': 'Amazonas', 'sigla': 'AM'},
    {'uf': 'Amapá', 'sigla': 'AP'}
]
for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'O valor de {k} é {v}.')
    for v in e.values():
        print(v, end=' ')
    print()  # apenas para quebrar p/ próxima linha

print(sep)

resultados = {'jogador1': 12, 'jogador2': 7, 'jogador3': 20, 'jogador4': 15}
# print(resultados)
# print(sorted(resultados))

from operator import itemgetter
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print(ranking)

medias = {'Pedro': 9.5, 'Juca': 5.0, 'Alfredo': 7.7, 'Helena': 6.0}
organiza = sorted(medias.items(), key=itemgetter(1))
print(organiza)
organiza = sorted(medias.items(), key=itemgetter(0))
print(organiza)
