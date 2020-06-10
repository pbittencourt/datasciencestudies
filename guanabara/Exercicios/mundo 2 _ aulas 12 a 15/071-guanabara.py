# SIMULADOR DE CAIXA ELETRÔNICO
# Guanabara version
# Não utiliza listas, boa ideia!

from time import sleep  # só pra fazer uma graça

print('$' * 50)
print('{:^50}'.format(' BANKOSTENTAÇÃO '))
print('{:^50}'.format('Aqui o seu dinheiro rende mais!'))
print('$' * 50, end='\n\n')

valor = int(input('Quer sacar quanto? _ R$ '))

total = valor   # montante a ser sacado
ced = 50        # primeira valor de cédula a ser retirado da máquina
totced = 0      # total de cédulas já retiradas

while True:     # começa o loop "infinito" de retirada
    if total >= ced:    # se o montante atual é superior ao valor atual da cédula, continua
        total -= ced    # retira uma cédula do montante
        totced += 1     # acrescenta 1 ao número de cédulas retirado
    else:               # não da pra tirar dinheiro com essa cédula, então diminua!
        if totced > 0:  # há cédulas a serem exibidas, então faça-o!
            print(f'Retirando {totced} cédulas de R$ {ced:.2f} ...')
            sleep(1)  # faz um suspensinho .... rsrsrs

        if ced == 50:
            # eu estava em R$50, ficou insuficiente, então desço para R$20
            ced = 20
        elif ced == 20:
            # mesma lógica que acima!
            ced = 10
        elif ced == 10:
            ced = 1

        # zera a quantidade de cédulas retiradas na instância atual
        totced = 0

        # quando o montante for zerado, interrompa o laço!
        if total == 0:
            break

print('_' * 50)
print('Operação finalizada. Tenha um bom dia!')