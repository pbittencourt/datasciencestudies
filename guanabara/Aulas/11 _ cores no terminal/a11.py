# BRINCANDO COM CORES!
''' ==================================
\033[ style; text; back m
style: 0    1    4    7
       norm bold undr invr
text:  30  31  32  33  34  35  36  37
       whi red grn yel blu mgn cyn gra
back:  40  41  42  43  44  45  46  47
       whi red grn yel blu mgn cyn gra
\033[ _;_;_m blablabla \033[m << reset
================================== '''

i = 0
j = 0
c = ['W','R','G','Y','B','M','C','K']
print('-' * 66)
while i < 8:
    lin = 30 + i
    print(f'{c[i]}: ', end='')
    while j < 8:
        col = 40 + j
        print(f'\033[{str(lin)};{str(col)}m {lin};{col} \033[m ', end='')
        j += 1
    print('\n' + '-' * 66)
    j = 0
    i += 1

colorido = 'Eike coisa linda!'
semcor = 'Tô contente.'
print(f'\033[1;30;44m{colorido}\033[m {semcor}')