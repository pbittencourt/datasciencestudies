alunos = [
    ['Pedro', [8, 9]],
    ['Jonas', [5.5, 4.34]],
    ['Maria', [9, 8.33]],
    ['Ana', [7.5, 8.5]]
]

for registro, valores in enumerate(alunos):
    print(f'({registro}) {valores}')
    nome = valores[0]
    n1 = valores[1][0]
    n2 = valores[1][1]
    media = (n1 + n2) / 2
    print(f'O estudante {nome} obteve as notas {n1:.1f} e {n2:.1f}, com média {media:.1f}.')