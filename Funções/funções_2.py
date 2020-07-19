#Passando argumentos
#Argumentos posicionais
def describe_pet(animal_type, pet_name):
    '''Exibe informações sobre um animal de estimação.'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet('hammster', 'harry')

# animal = input('\nQual o seu animalzinho? ')
# nome_pet = input('Qual o nome dele? ')
# describe_pet(animal, nome_pet)

#Várias chamadas de função
def describe_pet(animal_type, pet_name):
    '''Exibe informações sobre um animal de estimação.'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet('hammster', 'harry')
describe_pet('dog', 'willie')

#Argumentos nomeados
def describe_pet(animal_type, pet_name):
    '''Exibe informações sobre um animal de estimação.'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(animal_type = 'hammster', pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hammster')              #A ordem do argumento não importa em argumentos nomeados

#Valores default                                                        #Podemos ordenar somente o nome de um argumento por exemplo, caso o outro argumento for default
def describe_pet(pet_name, animal_type = 'dog'):
    '''Exibe informações sobre um animal de estimação.'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(pet_name = 'willie')
describe_pet('willie')                                                  #Com argumentos com valores default podemos chamar a função dessa forma mais simples

#Chamadas de função equivalentes
def describe_pet(pet_name, animal_type = 'dog'):
    '''Um cachorro chamado Willie'''
describe_pet('willie')
describe_pet(pet_name='willie')
'''Um hammster chamado Harry'''
describe_pet('harry','hamster')
describe_pet(pet_name='harry', animal_type='hamster')

'''
8.3 - Camiseta: Escreva uma função chamada make_shit() que aceite um tamanho e o texto de uma mensagem
que deverá ser estampada na camiseta. A função deve exibir uma frase que mostre o tamanho da camiseta
e a mensagem estamapda.'''
# print('\n8.3 - Camiseta')
# def make_shirt(tamanho,frase):
#     print('O tamanho da camiseta é ' + tamanho.title() + ' e a frase será: "' + frase.capitalize() + '" .')
# tamanho = input('Qual o tamanho da camiseta? ')
# frase = input('Qual a frase você gostaria de colocar nela? ')
# make_shirt(tamanho,frase)

'''
8.4 - Camisetas grandes: Modifique a função make_shirt() de modo que as camisetas sejam grandes por default, com uma 
mensagem Eu amo Python. Crie uma camiseta grande e outra média com a mensagem default, e uma camiseta de qualquer tamanho
com uma mensagem diferente.'''
print('\n8.4 - Camiseta grandes')
def make_shirt(tamanho = 'g',frase = 'eu amo python'):
    print('O tamanho da camiseta é ' + tamanho.title() + ' e a frase será: "' + frase.capitalize() + '" .')
make_shirt()
make_shirt(tamanho='m')
make_shirt(tamanho='p', frase= 'python rules')

'''
8.5 - Cidades: Escreva uma função chamada describe_city() que aceite o nome de uma cidade e seu pais. A função deve exibir
uma frase simples, como Reykjavik está localizada na Islândia. Forneça um valor default ao parâmetro que representa o país.
Chame sua função para três cidades diferentes em que pelo menos uma delas não esteja no país default.'''
print('\n8.5 - Cidades')
def describe_city(cidade,país = 'brasil'):
    print(cidade.title() + ' está localizada no(a) ' + país.title() + '.')
describe_city('mauá')
describe_city('santo andré')
describe_city('vancouver', país= 'canada')

