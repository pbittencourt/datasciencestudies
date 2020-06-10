# TRABALHANDO COM LISTAS

numeros = [1, 2, 5, 5, 3, 11, 8, 5]
print(numeros.count(5))
pos = list()
for j, n in enumerate(numeros):
    if n == 5:
        pos.append(j)
print(pos)

pedro = ['lindo', 'tesão', 'bonito']
print(pedro)
pedro.append('gostosão')
print(pedro)
pedro.insert(1, 'simpático')
print(pedro)
del pedro[1]
print(pedro)
pedro.pop(1)
print(pedro)
pedro.pop()
print(pedro)
pedro.remove('bonito')
print(pedro)

n = list(range(4,11,2))
print(n)

# python = ['linguagem', 'programação', 'roots', 'show']
# pythen = python  # faz uma cópia EMARANHADA
# pythen[2] = 'escrota'  # substitui em AMBAS as listas!
# print(f'Primeira lista: {python}')
# print(f'Segunda lista: {pythen}')

python = ['linguagem', 'programação', 'roots', 'show']
pythen = python[:]  # usando esse fatiamento estranho cria uma cópia ...
# pythen = python.copy()
pythen[2] = 'escrota'
print(f'Primeira lista: {python}')
print(f'Segunda lista: {pythen}')