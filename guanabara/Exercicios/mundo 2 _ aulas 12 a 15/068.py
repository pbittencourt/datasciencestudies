# PAR OU ÍMPAR
"""O jogo só finaliza quando o jogador perder para o computador.
Ao final, é exibido um placar (similar ao que foi feito no Adivinha 2.0)"""

from random import randint

print(f'{" PAR OU ÍMPAR? ":*^40}')

a = e = 0  # zera acertos e erros
nome = {'P': 'par', 'I': 'ímpar'}

while True:  # inicializa o laço
    j = int(input('Digite um número entre 0 e 10: _ '))
    o = str(input('Queres par ou ímpar? [P|I] ')).strip().upper()[0]

    # testa se o usuário escolheu algo fora das opções
    while o not in 'pPiI':
        print('Opção inválida!')
        o = str(input('Queres par ou ímpar? [P|I] ')).strip().upper()[0]

    c = randint(0, 10)      # "dedos" do computador
    s = j + c               # soma dos "dedos"

    # se a div da soma por 2 tiver resto 0, é par, senão é ímpar:
    r = 'P' if s % 2 == 0 else 'I'

    print(f'\nVocê jogou {j} e eu joguei {c}.')
    print(f'A soma de nossos dedos é {s}, ou seja, {nome[r]}!')

    if o == r:
        # jogador venceu
        print(f'Você pediu {nome[o]} também, então venceu essa rodada. Vamos continuar!')
        a += 1
        print('-' * 30)
    else:
        # jogador perdeu
        print(f'Você pediu {nome[o]}, então perdeu!')
        e += 1
        print('-' * 30)
        break   # quando o jogador perde, o laço é interrompido!

print('Fim do jogo! Placar final:\n\n' + '=' * 40 + f'\nVOCÊ {a} x {e} COMPUTADOR.\n' + '=' * 40)
print('\nObrigado pela brincadeira. Volte mais vezes! (:')
