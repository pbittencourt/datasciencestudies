# APROVEITAMENTO DE UM JOGADOR
"""Lê o nome de um jogador e quantas partidas ele disputou.
Para cada uma delas, anota a quantidade de gols marcados.
Em um dicionário, guardará nome, gols e total, na seguinte
estrutura:
{ nome, '', gols: [ ... ], total: __ }"""

jogador = dict()  # dados do jogador
gols = list()  # gols marcados a cada partida

# recebe nome e nº de partidas disputadas
nome = str(input('Nome do jogador: _ ')).strip().title()
num_partidas = int(input(f'Quantas partidas {nome} disputou? _ '))

# recebe quantidade de gols marcados a cada partida
for i in range(0, num_partidas):
    gols.append(int(input(f'Gols marcados na partida {i + 1}: _ ')))

# adiciona informações ao dicionário
jogador['nome'] = nome
jogador['gols'] = gols
jogador['total'] = sum(gols)
jogador['aproveitamento'] = float(sum(gols) / num_partidas)

# exibe na forma sequencial as informações do jogador
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

# exibe de forma mais detalhada as estatísticas do mesmo!
print(f'O jogador {jogador["nome"]} jogou {num_partidas} partidas.')
for i in range(0, len(jogador['gols'])):
    print(f'\t=> Na partida {i + 1}, marcou {jogador["gols"][i]} gols.')
print(f'{jogador["nome"]} fez um total de {jogador["total"]} gols, '
      f'com aproveitamento {jogador["aproveitamento"]:.2f} gol/partida.')
