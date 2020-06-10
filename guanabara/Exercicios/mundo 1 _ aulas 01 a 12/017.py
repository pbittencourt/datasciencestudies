from math import sqrt,hypot
c1 = float(input('Entre com o valor do primeiro cateto: '))
c2 = float(input('Entre com o valor do segundo cateto: '))
h = sqrt(c1**2 + c2**2)

print('A hipotenusa vale {:.2f}' .format(h))
print('Usando modulo: {:.2f}' .format(hypot(c1, c2)))