# PUDIM
"""Verifica se o site pudim.com.br está acessível ..."""""

from urllib import request

url = 'http://www.pudim.com.br'

try:
    site = request.urlopen(url)
except:
    print(f'''O site <{url}> \033[31mnão está acessível.\033[m''')
else:
    print(f'''O site <{url}> \033[32mestá acessível!\033[m''')
    fetch = site.read()
    print(type(fetch))
    # lines = fetch.split('\n')
    # print(lines)
