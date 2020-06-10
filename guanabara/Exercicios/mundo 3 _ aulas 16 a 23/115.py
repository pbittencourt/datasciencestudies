# CADASTRO DE PESSOAS EM ARQUIVO
"""Sistema modularizado que cadastra nome e idade de um usuário
em um arquivo de texto. Possui apenas as funções cadastrar e listar."""


from Exercicios.utilidades import cor
from Exercicios.utilidades import dado
from time import sleep


def linha(char='-', len=40):
    print(char * len)


def titulo(msg=''):
    linha()
    print(f'{msg.upper():^40}')
    linha()


def menu(* opcoes):
    if not len(opcoes) == 0:
        titulo('menu principal')
        for i, opcao in enumerate(opcoes):
            print(f'{cor.clr("[" + str(i + 1) + "]", "g")} _ {cor.clr(opcao, "b")}')
        linha()
        valido = False
        while not valido:
            try:
                opt = int(input(f'{cor.clr("Sua opção: _ ", "g")} '))
            except:
                sleep(0.3)
                print(f'{cor.clr("Por favor, digite um número inteiro válido.", "r")}')
                sleep(0.3)
            else:
                if 1 <= opt <= 3:
                    valido = True
                    return opt
                else:
                    sleep(0.3)
                    print(f'{cor.clr("Opção inexistente", "r")}')
                    sleep(0.3)


def listagem():
    titulo('pessoas cadastradas')
    try:
        arquivo = open('ex115a.txt')
    except:
        print(f'{cor.clr("Algo de inesperado ocorreu!", "r")}')
        print(f'{cor.clr("O arquivo não existe ou está corrompido.", "r")}')
        print(f'{cor.clr("Contate o administrador do sistema.", "r")}')
    else:
        linhas = arquivo.readlines()
        if len(linhas) == 0:
            print(f'{cor.clr("Ainda não há pessoas cadastradas.", "k")}')
        else:
            for linha in linhas:
                pessoa = linha.replace('\n', '').split('|')
                nome = pessoa[0]
                idade = pessoa[1]
                print(f'{nome:32} {idade:>2} anos')
        arquivo.close()
        sleep(1)


def cadastro():
    titulo('novo cadastro')
    arquivo = open('ex115a.txt', 'a')
    nome = dado.leianome(f'{cor.clr("Nome: _ ", "c")}')
    idade = dado.leiaidade(f'{cor.clr("Idade: _ ", "c")}')
    arquivo.write(nome + '|' + str(idade) + '\r')
    arquivo.close()
    print(f'{cor.clr(nome, "c")} adicionado\nao registro com sucesso!')
    sleep(1)


def encerra():
    linha()
    print(f'{cor.clr("Estamos encerrando o programa, aguarde ...", "k")}')
    sleep(1)
    print(f'{cor.clr("Verificando pendências no banco de dados ...", "c")}')
    sleep(1)
    print(f'{cor.clr("Congelando os módulos espaciais e temporais ...", "m")}')
    sleep(1)
    print()
    print(f'{cor.clr("TUDO CERTO!", "wg")}')
    print()
    sleep(0.5)
    print(f'{cor.clr("Obrigado por utilizar o CadastraGente!", "g")}')


while True:
    opt = menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')
    if opt == 1:
        listagem()
    elif opt == 2:
        cadastro()
    elif opt == 3:
        encerra()
        break

# fim do programa
