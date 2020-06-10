# CADASTRA PESSOAS LEVES E PESADAS
"""O usuário cadastra um certo número de pessoas e seus pesos,
até resolver finalizar o loop. Ao final, o programa exibe:
i)  Quantas pessoas foram cadastradas
ii) Uma lista com as pessoas que possuem
    o maior e o menor peso registrados"""

dado = []  # recebe o input do usuário
pessoas = []  # armazena as pessoas cadastradas
maior = menor = 0  # armazena maior e menor pesos
cont = 0  # contador do laço
listaMaior = ''  # lista as pessoas com o maior peso
listaMenor = ''  # lista as pessoas com o menor peso

while True:
    # recebe inputs do usuário, armazenando na lista "dado"
    # nome e peso, ocupando os índices 0 e 1
    dado.append(str(input('Nome: _ ')).strip().title())
    dado.append(float(input('Peso (em kg): _ ')))

    # acrescenta à lista "pessoas" uma cópia dos dados recebidos
    pessoas.append(dado[:])

    # se for a 1ª iteração do laço, o peso digitado é o menor valor
    # OU: se o peso digitado for menor do que o atual valor da variável
    # "menor", então atualize-a para receber o peso recebido
    if len(pessoas) == 1 or dado[1] < menor:
        menor = dado[1]

    # se o peso digitado for maior do que o atual valor da variável
    # "maior", atualize-a para receber o peso recebido
    if dado[1] > maior:
        maior = dado[1]

    # verifica se o usuário quer continuar
    while True:
        opt = str(input('Quer cadastrar outro usuário? [S|N] _ ')).strip().upper()[0]
        if opt in 'sSnN':
            break
        print('Entrada inválida!', end=' ')
    if opt == 'N':
        break

    # 'limpa' a lista que recebe inputs do usuário
    dado.clear()

print(f'\nForam cadastrados {len(pessoas)} usuários.')

# atualiza listas com pessoas que possuem menor e maior pesos
for pessoa in pessoas:
    if pessoa[1] == menor:
        listaMenor += '[' + pessoa[0] + '] '
    elif pessoa[1] == maior:
        listaMaior += '[' + pessoa[0] + '] '

print(f'O maior peso registrado foi de {maior:.2f} kg, peso de {listaMaior}.')
print(f'O menor peso registrado foi de {menor:.2f} kg, peso de {listaMenor}.')
