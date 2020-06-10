# FICHA DO JOGADOR
"""Recebe o nome do jogador e a quantidade de gols que fez.
No caso de campo em branco, retorna <<<Desconhecido>>>."""


def ficha(jogador='<<desconhecido>>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s).')


n = str(input('Nome do jogador: _ ')).strip().title()
g = str(input('Número de gols: _ ')).strip()

# verifica se o usuário digitou um número
if g.isnumeric():
	g = int(g)  # transforma o valor digitado em número
else:
	g = 0  # exibe zero em caso contrário

# verifica se o usuário digitou o nome do jogador
if len(n) > 0:
	ficha(n, g)
else:
	ficha()
