# ANALISANDO NOTAS E GERANDO UM DICIONÁRIO
"""Criação da função notas(), que pode receber várias notas de alunos
e gerar um dicionário com as seguintes informações: quantidade de notas,
maior nota, menor nota, média e situação do estudante (opcional)."""


def leianota(value='Digite um valor numérico: _ '):
    while True:
        numero = str(input(value))
        if numero.isalnum():
            return float(numero)
        print(f'\033[1;41m ERRO! \033[m',end=' ')


def notas(* nota, sit=False):
    """
    Recebe a analisa as notas de um estudante
    :param nota: as notas recebidas pelo estudante
    :param sit: exibir ou não a situação do estudante
    :return: {total, maior, menor, situação}
    """
    out = {
        'total': len(nota),
        'maior': max(nota),
        'menor': min(nota),
        'media': sum(nota) / len(nota)
    }
    if sit:
        if out['media'] >= 8:
            out['situacao'] = 'EXCELENTE'
        elif out['media'] >= 5:
            out['situacao'] = 'NA MÉDIA'
        elif out['media'] >= 3:
            out['situacao'] = 'PERIGANDO'
        else:
            out['situacao'] = 'TA NA MERDA RAPÁ'
    return out


print(notas(1.5, 6, 7.5, sit=True))
