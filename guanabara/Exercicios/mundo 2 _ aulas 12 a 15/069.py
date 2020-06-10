# EXIBINDO DADOS DE PESSOAS
"""O programa lê idade e sexo de várias pessoas. A cada iteração,
pergunta se o usuário quer ou não continuar o cadastro. Ao final, mostra:
i)   quantas pessoas têm mais de 18 anos
ii)  quantos homens foram cadastrados
iii) quantas mulheres têm menos de 20 anos"""

# inicializa variáveis para contar:
# usuarios cadastrados | pessoas +18 | homens | mulheres -20
usuario = maiores = homens = mulheres_abaixo_20 = 0

while True:
    usuario += 1
    print('-'*40)
    titulo = f'Cadastro do {usuario}º usuário'.upper()
    print(f'{titulo:^40}')
    print('-' * 40)

    idade = int(input(f'Digite a idade do {usuario}o usuário: _ '))
    sexo = str(input(f'Digite o sexo do {usuario}o usuário [M|F]: _ ')).strip().upper()[0]
    while sexo not in 'mMfF':
        sexo = str(input(f'Entrada inválida!\nDigite o sexo do {usuario}o usuário [M|F]: _ ')).strip().upper()[0]

    if idade > 18:
        maiores += 1
    if sexo in 'mM':
        homens += 1
    if sexo in 'fF' and idade < 20:
        mulheres_abaixo_20 += 1

    continuar = ' '  # deixa "vazio" para entrar no próximo loop
    while continuar not in 'sSnN':
        continuar = str(input('\nQuer cadastrar outro usuário? [S|N] _ ')).strip().upper()[0]
    if continuar in 'nN':
        break

print('='*40)
print(f'Foram cadastrados {usuario} usuários no sistema.')
print(f'Destes, {maiores} têm acima de 18 anos,', end=' ')
print(f'{homens} são homens e\n{mulheres_abaixo_20} são mulheres com menos de 20 anos.')
print('\n\nFim do programa! Volte sempre.')
