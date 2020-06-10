# MULTA DE VELOCIDADE

v = float(input('Qual a velocidade do carro: '))

if v > 80:
    m = 7 * (v - 80)
    print('PRÍÍÍ! Parado aí!! Você foi MULTADO em R$ {:.2f}' .format(m, '.2f'))
