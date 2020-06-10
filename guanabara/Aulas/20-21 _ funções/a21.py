# EXPLORANDO MAIS A IDEIA DE FUNÇÕES
""" =====================================================
1__ O mágico mundo das docstrings
2__ Parâmetros com valores default (parâmetros opcionais)
    Eu já havia explorado um pouco isto na aula anterior,
    no método tentativa-e-erro, então estamos suaves!
3__ Escopo de variáveis (global x local)
4__ Retorno de valores
    Eu também já tinha experimentado com retornos de
    valores nos estudos da aula 20.
===================================================== """


def contador(i, f, p):
    """
    **************************************
    * CONTADOR PERSONALIZADO             *
    * Faz uma contagem e mostra na tela  *
    * Função by PEDROLLA                 *
    **************************************
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='... ')
        c += p
    print('fim!')


def teste(b):
    global a  # definindo o escopo dessa variável como global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


def localiza():
    y = 5


# Chama a função contador e exibe uma ajuda
contador(2, 10, 2)
help(contador)

# Verificações de escopo de variáveis
a = 5  # após declarado GLOBAL na função, essa variável perdeu seu valor
teste(a)
print(f'A fora vale {a}')

x = 6
print(f'O valor de x é {x}.')
print(f'O valor de y, que está na função localiza, é {y}.')
