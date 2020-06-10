# CADÊ AS VOGAL?
"""Uma tupla armazena algumas palavras. O programa exibe,
para cada palavra, quais são suas vogais."""

palavras = ('fotografia', 'microfone,', 'computador', 'garrafa', 'livro', 'rbznsky', 'Arara')
vogais = 'aeiou'

for palavra in palavras:
    letras = len(palavra)
    print(f'A palavra {palavra.upper()} tem {letras} letras.')
    cont = 0
    for letra in palavra:
        if letra in vogais:
            cont += 1
    if cont > 0:
        print('Suas vogais são:')
        pos = 0
        for letra in palavra:
            pos += 1
            if letra.lower() in vogais:
                print(f'     {letra.lower()}, na {pos}ª posição;')
    else:
        print('Não há vogais nessa palavra. Esquisito, né?')
    print('-' * 40)
