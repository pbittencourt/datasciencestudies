from Exercicios.utilidades import dado
from lib.interface import *
from lib.arquivo import *
from time import sleep


# seleciona arquivo contendo a base de usuários
# e verifica sua existência. em caso negativo,
# cria o arquivo
arq = 'usuarios.txt'
if not existearquivo(arq):
    # cria um arquivo
    criaarquivo(arq)

# loop do programa principal
while True:
    # abre menu
    opt = menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')

    # listagem de arquivos
    if opt == 1:
        listagem(arq)

    # cadastro de novos usuários
    elif opt == 2:
        nome = dado.leianome(f'{cor.clr("Nome: _ ", "c")}')
        idade = dado.leiaidade(f'{cor.clr("Idade: _ ", "c")}')
        cadastro(arq, nome, idade)

    # encerra o programa
    elif opt == 3:
        encerra()
        break

    # usuário inseriu opção inexistente
    else:
        print(f'{cor.clr("Opção inexistente", "r")}')

    # pequeno delay para exibir novamente o menu
    sleep(1)

# fim do programa
