# MAIOR E MENOR PESO

print('Vamos ler o peso de CINCO pessoas!')

me = 0
ma = 0
p = 0
lista = []
for i in range(0, 5):
    p = float(input('Digite o peso (em kg) da {}a pessoa: _ ' .format(i + 1)))
    lista.append(p)
    if i == 0:
        me = p
    if p < me:
        me = p
    if p > ma:
        ma = p

print('Foram digitados os seguintes pesos:\n{}' .format(lista))
print('Observa-se, portanto, que o menor é {:.1f} kg e o maior é {:.2f} kg.' .format(me, ma))
