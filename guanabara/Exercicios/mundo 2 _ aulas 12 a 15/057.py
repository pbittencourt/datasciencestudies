# SOMENTE GÊNEROS CORRETOS!
# um pouco mais inclusivo do q o original :)

g = str(input('Insira seu gênero [M|F|T|Q|N]: _ ')).strip().upper()[0]
while g not in 'MFTQN':
    g = str(input('Formato incorreto! Tente novamente.\nInsira seu gênero [M|F|T|Q|N]: _ ')).strip().upper()[0]
print('Obrigado. Gênero {} registrado com sucesso!'.format(g))
