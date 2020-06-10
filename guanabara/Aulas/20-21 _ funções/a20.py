# INTRO ÀS FUNÇÕES! EBA!!

# função sem parâmetro
def linha():
    print('-' * 20)

linha()

# função com parâmetros
def mostraLinha(tamanho):
    print('_' * tamanho)

mostraLinha(40)
mostraLinha(10)

# função com parâmetros e padrões
def titulo(texto, tamanho = 40, sep = '='):
    print(sep * tamanho)
    print(f'{texto:^{tamanho * len(sep)}}'.upper())
    print(sep * tamanho)

titulo('eae mein blz?')
titulo('tudo legal kra?', 50, '-')
titulo('essa fera', 33)
titulo('títulão', sep=':;')
titulo(sep='.', texto='hihi', tamanho=14)

# função com empacotamento
def contador(* num):
    tam = len(num)
    print(f'Recebi {tam} valores: {num}')  # num é uma tupla!

contador(1, 5, 3)
contador(4, 2, 6, 1, 3)
contador(11)

# nas funções, parâmetros são passados por REFERÊNCIA
# (seriam os PONTEIROS do C++, por exemplo?!)
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [3, 6, 1, 4, 0]
print(valores)
dobra(valores)
print(valores)

def soma(* num):
    s = 0
    for n in num:
        s += n
    print(f'A soma de {num} é {s}')

soma(4)
soma(3, 7)
soma(1, 12, 9, -4)
