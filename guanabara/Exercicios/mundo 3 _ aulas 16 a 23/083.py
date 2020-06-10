# ANALISADOR DE EXPRESSÕES NUMÉRICAS
"""Verifica se o número de parênteses abertos corresponde ao número de parênteses fechados."""

exp = '((a+(b/c)) * ( f - (c-d + e) ) ^3 + )4)'
#exp = str(input('Digite uma expressão: _ ')).strip()
print(f'Você digitou a expressão: \033[1;30;45m {exp} \033[m.')

# fatiando a string em caracteres
fatia = list()
for i in exp:
    fatia.append(i)

abriu = fatia.count('(')  # qtd de parênteses abertos
fechou = fatia.count(')')  # qtd de parênteses fechados

if abriu != fechou:
    # número diferente de parênteses abertos e fechados
    # expressão inválida!
    print('Essa expressão é \033[1;30;41m inválida! \033[m')

    # exibe se foram abertos ou fechados mais parênteses
    if abriu > fechou:
        print(f'Você abriu {abriu} parênteses mas fechou apenas {fechou}.')
    else:
        print(f'Você fechou {fechou} parênteses mas apenas {abriu} foram abertos.')
else:
    # número igual de parênteses abertos e fechados
    # expressão válida!
    print('Essa expressão é \033[1;30;44m válida! \033[m')
    print(f'Você abriu e fechou {abriu} parênteses.')

print('=' * 30)
print('Solução alternativa do Guanabara')

pilha = []  # empilhamento de parênteses
for sym in exp:  # varre a string de expressão
    if sym == '(':
        # encontrou um parênteses aberto, então adiciona-o à pilha
        pilha.append(sym)
    elif sym == ')':
        # encontrou um parênteses fechado
        if len(pilha) > 0:
            # se a pilha já contiver elementos, remove um item da lista
            pilha.pop()
        else:
            # caso contrário, adiciona o parênteses fechado
            pilha.append(sym)

# ideia geral: cada parênteses aberto é inserido na pilha e cada
# parênteses fechado remove um parênteses aberto. a pilha correta,
# portanto, não deve conter elementos!
if len(pilha) == 0:
    # expressão válida!
    print('Essa expressão é \033[1;30;44m válida! \033[m')
else:
    # expressão inválida!
    print('Essa expressão é \033[1;30;41m inválida! \033[m')

print('Fim do programa (:')
