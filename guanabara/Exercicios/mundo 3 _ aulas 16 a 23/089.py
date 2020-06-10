# BOLETIM ESTUDANTIL
"""O programa lê nome e duas notas de vários alunos (até o usuário parar).
Ao final, mostra um boletim contendo média de cada estudante. Também permite
que se possa mostrar as notas individuais de cada aluno."""

from time import sleep

alunos = list()  # armazena todos os dados de todos os alunos

# loop de cadastro de alunos
while True:

    # recebe o input do usuário e cadastra no formato:
    # ['aluno', [n1, n2], média]
    nome = str(input('Nome: _ ')).strip().title()
    n1 = float(input('Nota 1: _ '))
    n2 = float(input('Nota 2: _ '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])

    # verifica se o usuário quer acrescentar +dados:
    while True:
        opt = str(input('Quer acrescentar dados de outro estudante? [S|N] _ ')).strip().upper()[0]
        if opt in 'SN':
            break
        print('Entrada inválida!', end=' ')
    if opt == 'N':
        break
# fim do loop

print('\n' + '=' * 30 + '\nGerando boletins... aguarde...\n')
sleep(2)

# cabeçalho dos boletins
print(f'nº  {"NOME":20} MÉDIA')
print('-' * 30)

# loop para exibir dados individuais de cada aluno
# n: índice do registro
# a: lista contendo dados do estudante
# formato [n, ['nome', [n1, n2], média ] ]
for n, a in enumerate(alunos):
    nome = a[0]
    media = a[2]
    print(f'{n:<3} {nome:20} {media:3.1f}')
    sleep(0.5)

# loop para exibir notas individuais de cada estudante
while True:
    print('-' * 30 + '\n')
    ind = int(input('Mostrar notas individuais de qual estudante? (999 interrompe) _ '))

    # opção 999 encerra o programa
    if ind == 999:
        print('Finalizando ...')
        sleep(1)
        break

    # verifica se o usuário entrou com um índice válido
    if ind <= len(alunos) - 1:
        # recebe dados do estudante
        nome = alunos[ind][0]
        n1 = alunos[ind][1][0]
        n2 = alunos[ind][1][1]

        # exibe os dados com um delay de entrada e saída,
        # só pra fazer uma gracinha rsrsrs ......
        sleep(0.3)
        print(f'As notas de {nome} foram: {n1:.1f} e {n2:.1f}.')
        sleep(1)
    # exibe mensagem de erro caso o usuário tenha digitado um ID inválido
    else:
        print('Entrada inválida!')

print('Obrigado por utilizar o SUPERNOTAS!')
