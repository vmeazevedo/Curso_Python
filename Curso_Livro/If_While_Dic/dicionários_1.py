#Um dicionário simples
alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

#Acessando valores em um dicionário
print()
alien_0 = {'color':'green'}
print(alien_0['color'])

print()
alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print(f'You just earned {str(new_points)} points!')

#Adicionando novos pares chave-valor
print()
alien_0 = {'color':'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Começando com um dicionário vazio
print()
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#Modificando valores em um dicionário
print()
alien_0 = {'color':'green'}
print(f'The alien is ' + alien_0['color'] + '.')

alien_0 = {'color':'yellow'}
print(f'The alien is now ' + alien_0['color'] + '.')

#Movimentando o alien
print()
alien_0 = {'x_position':0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: ' + str(alien_0['x_position']))
print(alien_0)

''' Move o alienigena para a direita
Determina a distância que o alienigena deve se desloca de acordo com sua velocida atual.'''
if alien_0['speed'] == 'slow':
    x_increment = 1
if alien_0['speed'] == 'medium':
    x_increment = 2
else:
    '''Este deve ser um alienigena rapido'''
    x_increment = 3

''' A nova posição é a posição antiga somada ao incremento'''
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))
print(alien_0)

#Removendo pares chave-valor
print()
alien_0 = {'color':'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

#Um dicionário de objetos semelhantes
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print('Sarah favorite language is ' + favorite_languages['sarah'].title() + '.')

'''
6.1 - Pessoa: Use um dicionario para armazenar informações sobre uma pessoa que você conheça. Armazene seu
primeiro nome, sobrenome, idade e cidade em que ela vive. Você deverá ter chaves como first_name, last_name
age e city. Mostre cada informação armazenada em seu dicionário.'''
print('\n6.1 - Pessoas')
info = {'first_name': 'vinicius', 'last_name':'azevedo', 'age': 28, 'city': 'mauá'}
print('Meu dicionário é: ')
print(info)
print('O primeiro nome é: ' + info['first_name'].title() + '.')
print('O ultimo nome é: ' + info['last_name'].title() + '.')
print('A idade é: ' + str(info['age']) + '.')
print('O nome da cidade é: ' + info['city'].title() + '.')

'''
6.2 - Números favoritos: Use um dicionario para armazenar os numeros favoritos de algumas pessoas.
Pense em cinco nomes e use-os como chaves em seu dicionarios. Pense em um numero favorito para cada
pessoa e armazene cada um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu numero
favorito. '''
print('\n6.2 - Números favoritos')
fav_number = {
    'nome1':'carlos','num1':1,
     'nome2':'iolanda', 'num2':2, 
     'nome3':'vinicius','num3':3, 
     'nome4':'marjorie','num4':4, 
     'nome5':'arthur', 'num5':5,
     }
print('O número favorito do ' + fav_number['nome1'].title() + ' é o ' + str(fav_number['num1']) + '.')
print('O número favorito da ' + fav_number['nome2'].title() + ' é o ' + str(fav_number['num2']) + '.')
print('O número favorito do ' + fav_number['nome3'].title() + ' é o ' + str(fav_number['num3']) + '.')
print('O número favorito do ' + fav_number['nome4'].title() + ' é o ' + str(fav_number['num4']) + '.')
print('O número favorito do ' + fav_number['nome5'].title() + ' é o ' + str(fav_number['num5']) + '.')

'''
6.3 - Glossário: Um dicionário Python pode ser usado para modelar um dicionario de verdade. No entanto,
para evitar confusão, vamos chamá-lo de glossário.'''
print('\n6.3 - Glossário')
dic = {
    'palavra1':'a','sign1':'a primeira letra do alfabeto', 
    'palavra2':'b','sign2':'a segunda letra do alfabeto', 
    'palavra3':'c','sign3':'a terceira letra do alfabeto', 
    }
print('Letra: ' + dic['palavra1'].title() + ' \nSignificado: ' + dic['sign1'].capitalize() + '.\n')
print('Letra: ' + dic['palavra2'].title() + ' \nSignificado: ' + dic['sign2'].capitalize() + '.\n')
print('Letra: ' + dic['palavra3'].title() + ' \nSignificado: ' + dic['sign3'].capitalize() + '.\n')

