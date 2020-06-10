# TABELA DO BRASILEIRÃO
"""Uma tupla armazena os 20 times da Série A do Brasileirão e retorna:
i)    Os cinco primeiros colocados
ii)   Os últimos 4 colocados
iii)  Uma lista com os colocados em ordem alfabética
iv)   Em qual posição está a Chapecoense"""

times = (
    'Palmeiras',
    'Santos',
    'Flamengo',
    'Atlético Mineiro',
    'Botafogo',
    'Atlético Paranaense',
    'Corinthians',
    'Ponte Preta',
    'Grêmio',
    'São Paulo',
    'Chapecoense',
    'Cruzeiro',
    'Fluminense',
    'Sport',
    'Coritiba',
    'Vitória',
    'Internacional',
    'Figueirense',
    'Santa Cruz',
    'América Mineiro'
)

linha = '-' * 50

# cabeçalho estilozinho
print('=' * 50 + '\n{:^50}'.format('CAMPEONATO BRASILEIRO DE FUTEBOL') + '\n{:^50}\n'.format('Anno de 2016') + '=' * 50)

print('Os cinco primeiros colocados foram:')
for i in range(0, 5):
    campeao = '[CAMPEÃO]' if i == 0 else ''
    print(f'{i + 1}º colocado: {times[i]} {campeao}')

print(linha)
print('Os quatro últimos colocados foram:')
for i in range(times.index(times[-4]), len(times)):
    print(f'{i + 1}º colocado: {times[i]}')

print(linha)
print('A lista das equipes em ordem alfabética é:')
ordem = sorted(times)
for i in ordem:
    print(i)

print(linha)
equipe = 'chapecoense'
print(f'A equipe {equipe.upper()} se encontra na {times.index(equipe.capitalize()) + 1}ª posição da lista.')
