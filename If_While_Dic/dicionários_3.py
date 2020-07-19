#Informações aninhadas
#Uma lista de dicionários
alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color':'yellow', 'points': 10}
alien_2 = {'color':'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#Exemplo realista
print()
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print('Total number os aliens: ' + str(len(aliens)))

#Exemplo realista 2
print()
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

for alien in aliens[0:5]:
    print(alien)
print('...')


#Uma lista em um dicionário
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print('You ordered a ' + pizza['crust'] + '-crust pizza ' + 'with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)


print()
favorite_languages = {
    'jen':['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite language are: ")
    for language in languages: 
        print('\t' + language.title())


#Um dicionário em um dicionário
print('\nDicionário dentro de um dicionário.')
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())

'''
6.7 - Pessoas: Comece com o programa que você escreveu na pag 147. Crie dois novos dicionarios que represetem pessoas diferentes e armazene os tres
dicionarios em uma lista chamada people. Percorra sua lista de pessoas com um laço. A medida que percorrer a lista, apresente tudo que voce sabe sobre
cada pessoa.'''

print('\n6.1 - Pessoas')
info_0 = {
    'first_name': 'vinicius', 
    'last_name':'azevedo', 
    'age': 28, 
    'city': 'mauá'}
info_1 = {
    'first_name': 'marta', 
    'last_name':'azevedo', 
    'age': 33, 
    'city': 'santo andre'}
info_2 = {
    'first_name': 'roberto', 
    'last_name':'azevedo', 
    'age': 44, 
    'city': 'sao caetano'}

people = [info_0, info_1, info_2]

for p in people:
    print(p)


'''
6.8 - Animais de Estimação: Crie varios dicionários, em que o nome de cada dicionario seja o nome de um animal de estimação.
Em cada dicionario, inclua o tipo de animal e o nome do dono. Armazene esses dicionarios em uma lista chamada pets.
Em seguida, percorra sua lista com um laço e, a medida que fizer isso, apresente tudo o que você sabe sobre cada animal de estimação.'''

'''
6.9 - Lugares favoritos: Crie um dicionario chamado favorite_places. Pense em tres nomes para usar como chaves do dicionario e armazene de
um a tres lugares favoritos para cada pessoa. Percorra o dicionario com um laço e apresente o nome de cada pessoa e seus lugares favoritos.'''
print('\n6.9 - Lugares favoritos')
favorites_places = {
    'vinicius': ['casa', 'sofa', 'quarto'],
    'roberto': ['praia', 'campo', 'ar'],
    'marta': ['abc', 'def', 'ghi'],
}

for nomes, lugares in favorites_places.items():
    print('Os lugares favoritos do ' + nomes.title() + ' são: ')
    for lugar in lugares:
        print(lugar.title())

'''
6.10 - Numeros favoritos: Modifique o seu programa da pag 147 para que cada pessoa possa ter mais de um numero favorito. Em seguida, apresente
o nome de cada pessoa, juntamente com seus numeros favoritos.'''
print('\n6.10 - Números favoritos')
fav_number = {
    'carlos': ['1', '11', '111'],
    'iolanda': ['2', '22', '222'],
    'vinicius': ['3', '33', '333'],
    'marjorie': ['4', '44', '444'],
    'arthur': ['5', '55', '555'],
}

for nomes, numeros in fav_number.items():
    print('Os numeros favoritos de ' + nomes.title() + ' são: ')
    for num in numeros:
        print('\t'+num)

'''
6.11 - Cidades: Crie um dicionário cities. Use os nomes de três cidades como chaves em seu dicionario. Crie um dicionario com informações sobre cada cidade
e inclua o pais em que a cidade esta localizada, a população aproximadas e um fato sobre a cidade. As chaves do dicionario de cada cidade devem ser algo
como country, population e fact. Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela.'''
cities = {
    'maua':{
        'country':'Brasil',
        'population':'Muito',
        'fact':'é bem feio',
    },
    
    'santo andre':{
        'country':'Brasil',
        'population':'pouco',
        'fact':'é bem zoado',
    },

    'londrina':{
        'country':'Brasil',
        'population':'quase',
        'fact':'so tem japones',
    },
}

for cidade, info in cities.items():
    print('\nCidade: ' + cidade.title())
    pais = info['country']
    população = info['population']
    fatos = info['fact']
    print('\tPaís: ' + pais.title())
    print('\tPopulação: ' + população.title())
    print('\tFatos: ' + fatos.capitalize())
