# IMPRIME UM NÚMERO POR EXTENSO
"""O programa lê uma tupla contendo números por extenso,
de 0 a 20. A partir do pedido do usuário, exibe-o"""

nome = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:  # laço para repetir o programa ao final se o usuário quiser
    while True: # laço para validar a entrada do usuário
        n = int(input('Digite um número entre 0 e 20: _ '))
        if 0 <= n <= 20:
            break
        print('Entrada inválida! ',end='')

    # imprime o número por extenso
    print(f'Você digitou o número {nome[n]}.')

    # verifica se o usuário quer imprimir outro número
    continuar = ' '
    while continuar not in 'SN':  # valida se a resposta foi sim ou não
        continuar = str(input('Você quer tentar outra vez? [S|N] _ ')).upper().strip()[0]
    if continuar == 'N':
        break

print('Fim do programa!')
