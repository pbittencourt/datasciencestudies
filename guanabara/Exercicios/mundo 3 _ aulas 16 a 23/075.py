# MAIS DADOS EM UMA TUPLA
"""O programa lê quatro números digitados pelo usuário e armazena-os numa tupla. Ao final, exibe:
i)   Quantas vezes apareceu o número 9
ii)  Em qual posição foi digitado o 1º 3
iii) Quais foram os números pares"""

# versão inicial minha
'''# os números são inseridos pelo usuário:
n1 = int(input('Digite um número: _ '))
n2 = int(input('Digite outro número: _ '))
n3 = int(input('Digite mais um número: _ '))
n4 = int(input('Digite o último número: _ '))

# armazena os valores na tupla 'lista' (eu gosto +de listas rsrs)
lista = (n1, n2, n3, n4)
print(f'Você digitou os valores {lista}.')'''

# sugestão mais sensata do prof:
lista = (
    int(input('Digite um número: _ ')),
    int(input('Digite outro número: _ ')),
    int(input('Digite mais um número: _ ')),
    int(input('Digite o último número: _ '))
)

# verifica se o número 9 foi digitado
if 9 not in lista:
    print('O valor 9 não foi digitado.')
else:
    plural = '' if lista.count(9) == 1 else 'es'  # pra exibir plural direito
    print(f'O valor 9 apareceu {lista.count(9)} vez{plural} na tupla.')

# verifica se o número 3 foi digitado
if 3 not in lista:
    print(f'O valor 3 não aparece em nenhuma posição da tupla.')
else:
    print(f'O valor 3 aparece na {lista.index(3) + 1}ª posição da tupla.')

# verifica quantos são pares
pares = 0
for i in lista:
    if i % 2 == 0:
        pares += 1
if pares != 0:
    print(f'Foram digitados {pares} valores pares: ', end='')
    for i in lista:
        if i % 2 == 0:
            print(i, end=' ')
else:
    print(f'Não foram inseridos valores pares.')
