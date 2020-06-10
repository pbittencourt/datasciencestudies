def line(char='-', size=40):
    print(char * size)


def title(text=''):
    line()
    print(f'{text.upper():^40}')
    line()


def section(title='', paragraph='', size=40, char='-'):
    """
    AINDA PRECISA TERMINAR ESSA MERDA
    :param title:
    :param paragraph:
    :param size:
    :param char:
    :return:
    """
    print(char * size)
    print(f'{title.upper().center(size)}')

    words = paragraph.split()
    # c = 0
    # for word in words:
    #     print(f'[{c}] ({len(word)}) {word}')
    #     c += 1

    empty_space = size
    i = 0
    while empty_space > 0:
        if (len(words[i])) < empty_space:
            # ainda tem espaço: imprime
            print(words[i], end=' ')
            i += 1
            empty_space -= len(words[i])
        else:
            print()
            empty_space = size

    print(char * size)
