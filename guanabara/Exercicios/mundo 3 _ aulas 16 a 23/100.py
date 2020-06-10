# SORTEIOS E FUNÇÕES
"""O programa contém uma lista e duas funções: sorteio() e somaPar().
A primeira função sorteia 5 números e os coloca na lista. A segunda
mostra a soma de todos os valores pares sorteados pela anterior."""


from random import randint


def sorteia(lst):
    # MODIFICA uma lista pré-existente, alterando seus elementos
    # para números aleatórios entre 1 e 10
    for i in range(0, 5):
        lst[i] = randint(1, 10)


def sorteio(lst, qtd=5, i=1, f=10):
    # CRIA uma lista contendo qtd elementos sorteados (de i a f)
    for i in range(0, qtd):
        lst.append(randint(i, f))


def somaPar(lst):
    # retorna a soma dos números pares contidos numa lista
    s = 0
    for i in lst:
        if i % 2 == 0:
            s += i
    return s


numeros = [1, 4, 2, 5, 3]
print(f'Lista original: {numeros}')
sorteia(numeros)
print(f'Lista sorteada: {numeros}')
print(f'A soma dos pares é {somaPar(numeros)}')

outro = list()
sorteio(outro, 7)
print(f'Mais uma lista, já sorteada: {outro}.')
print(f'Seus pares, somados, resultam em {somaPar(outro)}.')
