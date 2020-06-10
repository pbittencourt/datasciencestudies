# TL;DR: https://docs.python.org/3/library/exceptions.html

try:
    x = int(input('Numerador: _ '))
    y = int(input('Denominador: _ '))
    r = x / y
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível a divisão por zero.')
except KeyboardInterrupt:
    print('Programa interrompido pelo usuário')
except Exception as erro:
    print('Ih, rapaz, aconteceu alguma coisa estranha ...')
    print(f'O erro encontrado foi {erro.__cause__}.')
else:
    print(f'A divisão entre {x} e {y} é igual a {r:.1f}')
finally:
    print('Fim deste bloco!')