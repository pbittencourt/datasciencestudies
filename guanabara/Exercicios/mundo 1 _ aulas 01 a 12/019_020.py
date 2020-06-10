import random

num = int(input('Agora, utilizando loops! Quantos alunos vc quer: '))
i: int = 0
lista = []
while i < num:
    lista.append(input('Digite o nome do {}o aluno: ' .format(i+1)))
    i += 1
print(lista)
e = random.choice(lista)
print('Escolhemos o(a) {}!!! PARABÉNS!!1!!111!' .format(e))

print('-' * 12)

num = int(input('Vamos a mais um sorteio. Digite o número de alunos: '))
i: int = 0
lista = []
while i < num:
    lista.append(input('{}o estudante: ' .format(i+1)))
    i += 1
print(lista)
random.shuffle(lista)
print(lista)