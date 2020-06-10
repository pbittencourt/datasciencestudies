# APROVEITAMENTO DE UM JOGADOR v2.0
"""Lê o nome de um jogador e quantas partidas ele disputou.
Para cada uma delas, anota a quantidade de gols marcados.
Em um dicionário, guardará nome, gols e total, na seguinte
estrutura:
{ nome, '', gols: [ ... ], total: _, aproveitamento: _ }

Aprimora o programa 093, lendo de vários jogadores, até o usuário
interromper o laço. Exibe, ao final, uma tabela, contendo
cod  nome  gols  total
e um prompt para mostrar levantamento de 'qual jogador?'"""

from time import sleep

cadastro = list()  # armazena o cadastro de todos os jogadores
jogador = dict()  # armazena dados de cada jogador
gols = list()  # armazena gols de cada jogador
sep = '-' * 40  # linha separadora

while True:  # loop p/ cadastro de jogadores

    # linha separadora
    print(sep)

    # recebe o nome do jogador
    nome = str(input('Nome do jogador: _ ')).strip().title()

    # recebe os gols marcados a cada partida
    # num_partidas: número de partidas disputadas
    # gols_partida: gols marcados a cada partida
    # total_gols: total de gols marcados em todas as partidas
    num_partidas = int(input(f'Quantas partidas {nome} disputou? _ '))
    gols_partida = 0
    total_gols = 0
    for i in range(0, num_partidas):
        gols_partida = int(input(f'Gols marcados na partida {i + 1}: _ '))
        total_gols += gols_partida

        # acrescenta o número de gols marcados nesta partida
        # à lista contendo todos os gols deste jogador
        gols.append(gols_partida)
        # print(gols)

    # monta o dicionário jogador{}
    jogador['nome'] = nome
    jogador['gols'] = gols.copy()
    jogador['total'] = total_gols
    jogador['aproveitamento'] = float(total_gols / num_partidas)

    # acrescenta jogador{} ao cadastro[]
    cadastro.append(jogador.copy())

    # limpa p/ próxima iteração
    gols.clear()
    jogador.clear()

    # verifica se o usuário quer continuar
    while True:
        opt = str(input('Continuar? [S|N] _ ')).strip().upper()[0]
        if opt in 'SN':
            break
        print('Entrada inválida!', end=' ')
    if opt == 'N':
        break
# fim do cadastro de jogadores

print(sep + '\n')

# exibe tabela com o cadastro completo
print(f'cód  {"nome":<15}  {"gols":<15}  total  aprov')
print(f'{"":=^3}  {"":=^15}  {"":=^15}  {"":=^5}  {"":=^5}')
for j in range(0, len(cadastro)):
    nome = cadastro[j]['nome']
    gols = str(cadastro[j]['gols'])
    total = cadastro[j]['total']
    aprov = cadastro[j]['aproveitamento']
    print(f'{j:>3}  {nome:<15}  {gols:<15}  {total:^5}  {aprov:^5.1f}')

while True:  # prompt para exibir dados de um jogador específico

    # verifica de qual jogador queremos estatísticas
    # também faz validação de código digitado
    while True:
        j = int(input('\nMostrar dados de qual jogador? (999 para sair) _ '))
        if j > (len(cadastro) - 1) and j != 999:
            # inseri valor maior do que o último cadastro,
            # mas não inseri o flag de parada (999)
            print(f'Erro! Não existe jogador com código {j}. Tente novamente.')
        else:
            # se ñ pedir pra encerrar nem digitar código incorreto,
            # quebra esse laço e continua c/ o programa!
            break

    # digitando 999, encerra-se o programa
    if j == 999:
        print('\n' + sep)
        print('Encerrando ...')
        sleep(1)
        print('OBRIGADO por utilizar o JOGADADOS!')
        sleep(1)
        break

    # armazena dados em variáveis mais legíveis
    nome = cadastro[j]['nome']
    gols = cadastro[j]['gols']
    total = cadastro[j]['total']
    aprov = cadastro[j]['aproveitamento']

    # exibe as estatísticas do jogador
    print(f'LEVANTAMENTO do jogador \033[1m{nome}\033[m:')
    sleep(0.5)
    for k, v in enumerate(gols):
        print(f'\t=> No jogo {k + 1} fez {v} gols.')
        sleep(0.5)

    print(f'Marcou {total} gols em {len(gols)} partidas, com aproveitamento de {aprov:.2f} gols/partida.')
    sleep(0.5)

# fim do prompt e do programa
