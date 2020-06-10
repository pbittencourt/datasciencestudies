# SITUAÇÃO DO ESTUDANTE
"""Lê nome e média de um aluno, guardando também a situação deste
num dicionário. Ao final, mostra o conteúdo da estrutura na tela."""

nome = str(input('Nome do estudante: _ ')).strip().title()
media = float(input(f'Média de {nome}: _ '))
situacao = 'aprovado' if media >= 6 else 'reprovado'

estudante = {
    'nome': nome,
    'media': media,
    'situacao': situacao
}

print(estudante)

print(f'{"NOME":^20} {"MÉDIA":^7} {"SITUAÇÃO":^10}')
print('=' * 20 + ' ' + '=' * 7 + ' ' + '=' * 10)
print(f'{estudante["nome"]:<20} {estudante["media"]:^7.1f} {estudante["situacao"]:>10}')
