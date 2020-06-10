name = input('Digite seu nome: ')
city = input('Digite a cidade em q vc mora: ')

print(name.lower().find('leite'))
print(city.lower().find('santo'))

if name.lower().find('leite') != 1:
    print('Ai, leitinho....')

if city.lower().find('santo') != -1:
    print('Ui, santa..........')