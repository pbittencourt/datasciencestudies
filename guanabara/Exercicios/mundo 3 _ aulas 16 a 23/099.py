# QUAL É O MAIOR?
"""A função recebe vários parâmetros e retorna o maior deles"""


from time import sleep


def delay(texto, fim='\n', tempo=0.5):
    # exibe uma mensagem e dá um sleep em seguida
    # pode-se escolher o tempo, em milisec
    # tb da a possibilidade de quebrar linha ou não em seguida
    print(texto, end=fim)
    sleep(tempo)


def maior(*n):
    m = 0
    delay(f'Analisando os valores passados ...', tempo=1)
    for numero in n:
        delay(numero, ', ')
        if numero > m:
            m = numero
    delay('ok!', tempo=1)
    delay(f'Foram informados {len(n)} valores ao todo.')
    delay(f'O maior valor informado foi {m}.')
    delay('-' * 30)


# Analisa o maior número em alguns cenários diferentes
maior(3, 4)
maior(0, 11, -9, 20)
maior(6, 6, 6)  # editado no ubuntu
maior(5)
maior()
