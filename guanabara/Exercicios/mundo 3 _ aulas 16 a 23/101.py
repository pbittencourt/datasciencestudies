# VOTO
"""Uma função voto() recebe como parâmetro o ano de nascimento
de uma pessoa e retorna, com base na idade da pessoa, se o voto
é negado (-16), obrigatório (18~65) ou opcional (16~18 +65)."""


from datetime import date


def voto(ano):
    """
    Calcula a idade da pessoa e retorna se ela está apta a votar.
    :param ano: ano em que a pessoa nasceu
    :return: negado (idade < 16), obrigatório (18 <= idade <= 65)
    ou opcional (16 <= idade < 18 ou idade > 65)
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        situacao = 'negado'
    elif 18 <= idade <= 65:
        situacao = 'obrigatório'
    else:
        situacao = 'opcional'

    return situacao


ano = int(input('Em qual ano você nasceu? _ '))
print(f'Com {date.today().year - ano} anos, o voto é {voto(ano)}.')
