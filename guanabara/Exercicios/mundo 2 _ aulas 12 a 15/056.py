# QUATRO PESSOAS

soma = 0
novas = 0
velho_idade = 0
velho_nome = ''

nomes = []
sexos = []
idades = []

for c in range(0, 4):
    print('===== {}a PESSOA ====' .format(c + 1))
    nome = str(input('Nome: _ ')).strip()capitalize()
    nomes.append(nome)
    sexo = str(input('Sexo (M|F): _ ')).strip().upper()
    sexos.append(sexo)
    idade = int(input('Idade: _ '))
    idades.append(idade)

    soma += idade

    if sexo == 'M':
        if idade > velho_idade:
            velho_nome = nome
    else:
        if idade < 20:
            novas += 1

print('Foram digitados os seguintes nomes:')
print(nomes)
print('Suas idades são:')
print(idades)
print('Observa-se, então, que a idade média do grupo é {:.1f} anos,\no homem mais velho se chama {} e há {} mulheres com menos de 20 anos.' .format((soma / 4), velho_nome, novas))