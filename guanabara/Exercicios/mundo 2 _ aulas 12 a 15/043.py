# IMC

a = float(input('Qual é a sua altura, em metros? _ '))
p = float(input('Qual é o seu peso, em quilogramas? _ '))

imc = p / (a ** 2)

print('Seu IMC é {:.1f} e você está dentro do nível considerado' .format(imc), end = ' ')

if imc > 40:
    print('obesidade mórbida.')
elif imc > 30:
    print('obesidade.')
elif imc > 25:
    print('sobrepeso.')
elif imc > 18.5:
    print('peso ideal.')
else:
    print('abaixo do peso.')
