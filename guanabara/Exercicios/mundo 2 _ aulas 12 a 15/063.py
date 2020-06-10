# FIBONACCI agains
# vamos ver se dessa vez rola direito!

print('{:=^41}'.format(' sequência de fibonacci '.upper()))
n = int(input('Digite a quantidade de termos: _ '))

aant = 0            # PRIMEIRO TERMO
ant = 1             # SEGUNDO TERMO
c = 3               # ENTÃO COMEÇA A CONTAR NO 3º TERMO
lista = [aant, ant] # matriz pra guardar a sequencia
s = aant + ant      # soma dos termos (opcional meu)

print('-' * 40)
print('Os {} primeiros termos da sequência de Fibonacci são:\n0, 1, '.format(n),end='')

while c <= n:
    num = ant + aant
    aant = ant
    ant = num
    s += num
    lista.append(num)
    print(num, end='')
    if c == (n - 1):
        print(' e ', end='')
    elif c == (n):
        print('.')
    else:
        print(', ', end='')
    c += 1

print('A soma desses {} primeiros termos é {}.'.format(n, s))
print('Fim do programa')
