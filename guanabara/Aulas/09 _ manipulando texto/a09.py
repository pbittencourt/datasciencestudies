# Curso em vídeo Python
# 012345678901234567890
frase = 'Curso em vídeo Python'
zoado = '    eita cauboi viado  '
print(frase[9:21:2])
print(frase[9::2]) # same as above
print(frase[:5])
print(frase[15:])
print(frase.count('o'))
print(frase.count('o',0,14))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print('Android' in frase)
print(len(frase))
print(frase.replace('Python', 'Android'))
print(len(frase))
print(len(frase.replace('Python', 'Android')))
print(frase.capitalize())
print(frase.title())

print(zoado)
print(zoado.strip() + '!')
print(zoado.lstrip() + '!')
print(zoado.rstrip() + '!')

moses = "moses supposes his toeses are roses"
lista = moses.split()
print(moses.split())
print('-'.join(moses))
numoses = '-'.join(lista)
print(numoses)