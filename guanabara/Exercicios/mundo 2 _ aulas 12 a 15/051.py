# PROGRESSÃO ARITMÉTICA

a1 = int(input('Primeiro termo: _ '))
r = int(input('Razão: _ '))
a = []
s = 0

for n in range(1, 11):
    an = a1 + (n - 1) * r
    a.append(an)
    s += an

print('Os dez primeiros termos dessa PA são:')
print(a)
print('A soma desses termos é {}.' .format(s))

print('\n{:=^30}\n' .format(' Outro jeito ').upper())

b = []
z = 0
for n in range(a1, (a1 + 10 * r), r):
    b.append(n)
    z += n

print(b)
print(z)
