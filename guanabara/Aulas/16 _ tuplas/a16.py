# TUPLAS
# to sum up: (), [] e {} >> tupla, lista, dicionário

pedro = ('Lindo', 'Tesão', 'Bonito', 'Gostosão')

print(pedro)
print(sorted(pedro))
print(pedro)

for i in pedro:
    print(i)

print(i)  # último valor lido antes de encerrar o loop

for i in range(0, len(pedro)):
    print(f'{i}: {pedro[i]}')

print(pedro[1])
print(pedro[-1])
print(pedro[2:])
print(pedro[:2])
print(pedro[-3:])
print(pedro[:])

for pos, qualidade in enumerate(pedro):
    print(f'Ele é {pos + 1}: {qualidade}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(c)
print(c.count(4))
print(c.count(2))
print(c.count(9))
print(c.index(4))
print(c.index(2))
print(c.index(2, 1))

sujeito = ('Pedro', 32, 'M', 60.25)
print(sujeito)
del(sujeito) # tuplas são imutáveis POREM apagaveis!
'''
O código a seguir gera o erro
print(sujeito)
Traceback (most recent call last):
    print(sujeito)
NameError: name 'sujeito' is not defined
'''