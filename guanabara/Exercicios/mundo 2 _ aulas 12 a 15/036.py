# EMPRÉSTIMO

n = str(input('Digite seu nome para começarmos: _ '))
print('Olá, {}! Tudo bem?' .format(n))

c = float(input('Qual é o valor da casa? R$ '))
s = float(input('Quanto você ganha por mês? R$ '))
a = int(input('Em quantos anos você pretende quitar a casa? _ '))

p = c / (a * 12)

if p > (0.3 * s):
    print('Seu empréstimo foi negado, pois a parcela, de valor R$ {:.2f}, excede 30% de seu salário!' .format(p))
else:
    print('Empréstimo aprovado! Você pagará {} parcelas de R$ {:.2f} ao longo dos próximos {} anos.' .format(12 * a, p, a))