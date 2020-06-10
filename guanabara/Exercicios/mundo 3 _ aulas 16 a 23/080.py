# CADASTRANDO EM ORDEM!
"""O usuário cadastrará cinco valores numéricos, já na
posição correta da lista, sem utilizar o método sort()."""

numeros = list()  # armazena os números digitados

for i in range(0, 5):  # loop principal

    n = int(input('Digite um valor numérico: _ '))
    pos = i  # armazena a posição em que a lista se encontra

    for j in numeros:  # loop secundário, percorre a lista atual

        # somente interromperá o laço quando encontrar uma posição
        # na qual o valor digitado for inferior a algum valor
        # encontrado na lista
        if n < j:
            pos = numeros.index(j)
            break

    # insere o valor na lista, na posição anteriormente definida
    numeros.insert(pos, n)
    # (vale notar que, caso nada for encontrado, pos já havia sido
    # atribuido como i, então adiciona ao final da lista)

    # para exibir em qual posição da lista o valor foi adicionado
    ins = f'na \033[7mposição {pos}\033[m' if pos < i else '\033[7mao final\033[m'
    print(f'Valor {n} adicionado {ins} da lista!')

    # saída com a lista atual (opcional p/ controle)
    print(f'Lista atual: {numeros}.')

print('_'*30)
print(f'Lista finalizada: {numeros}.')
