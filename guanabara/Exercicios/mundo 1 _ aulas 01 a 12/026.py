frase = input('escreve algo ae: ')
letras = frase.lower().count('a')

print('A letra A aparece {} vezes nessa frase!' .format(letras))

j = 0
lista = []
for i in frase.lower():
    if i == 'a':
        lista.append(j)
    j += 1

print('Mais especificamente, ela aparece nas posições {}!!' .format(lista))

pri = frase.lower().find('a') + 1
ult = frase.lower().rfind('a') + 1

print('A primeira ocorrência se dá na posição {} e a última se dá na posição {} (:' .format(pri,ult))