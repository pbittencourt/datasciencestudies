# PROGRESSÃO ARITMÉTICA com while v2.0

print('=' * 44)
print('{:^44}'.format(' PROGRESSÃO ARITMÉTICA '))
print('{:^44}'.format('Exibindo os dez primeiros termos de uma PA'))
print('=' * 44)

a1 = int(input('Primeiro termo: _ '))
r = int(input('Razão: _ '))
an = a1     # enésimo termo (inicia igual ao primeiro)
a = []      # matriz pra guardar todos os termos (opcional meu)
n = 1       # inicia o contador de termos
t = 0       # total de termos (começa em zero para ser somado ao 'mais')
m = 10      # quantos serão exibidos 'a mais' (começa valendo 10)

while m != 0:
    t += m      # soma 'mais' ao total

    while n <= t:
        a.append(an)
        print('{}'.format(an), end='')
        print(', ' if n != t else '.', end='')
        an += r
        n += 1

    print('\n' + '-' * 30)
    m = int(input('Quer exibir mais quantos termos? (digite 0 para sair) _ '))

print('\nA PA completa, de razão {} e iniciando em {},\nficou com {} termos e pode ser conferida a seguir:\n{}'.format(r, a1, t, a))
print('Fim do programa!')
