# CONTADOR PERSONALIZADO
"""Cria uma função contador que recebe 3 parâmetros:
início, fim e passo, e realiza a contagem em três cenários:
i)   de 1 a 10, 1 em 1
ii)  de 10 a 0, de 2 em 2
iii) após input do usuário"""


from time import sleep


def linha():  # exibe linhas ao longo do programa
    print('\\=/=' * 10)


def contador(inicio, fim, passo):
    saida = inicio  # variável que a função retorna
    if passo < 0:  # se o passo for negativo, troca o sinal
        passo = -passo
    elif passo == 0:  # se o passo for nulo, torna-o igual a 1
        passo = 1

    # exibe a contagem
    print(f'Contando de {inicio} a {fim}, de {passo} em {passo}:')

    if fim > inicio:  # contador crescente, somaremos o passo
        while saida <= fim:
            print(saida, end=', ')
            sleep(0.5)
            saida += passo
    else:  # contador decrescente, subtrairemos o passo
        while saida >= fim:
            print(saida, end=', ')
            sleep(0.5)
            saida -= passo
    print('FIM!')


linha()
contador(1, 10, 1)  # indo de 1 a 10, de 1 em 1

linha()
contador(10, 0, 2)  # voltando de 10 a 0, de 2 em 2

linha()
print('Agora é com você:')
while True:  # pede para o usuário definir a contagem
    i = int(input('\nInício: '))
    f = int(input('Fim:    '))
    p = int(input('Passo:  '))
    contador(i, f, p)

    opt = str(input('\nPressione qualquer tecla para continuar ou N para interromper _ ')).strip().upper()[0]
    if opt == 'N':
        print('OBRIGADO POR TER JOGADO!')
        break

# fim do programa
