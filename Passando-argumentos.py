print('\nARGUMENTOS POSICIONAIS')
#É necessário informar os dados corretamente posicionados ao chamar a função
def describe_pet(animal_type, pet_name):
    '''Exibe informações sobre um animal de estimação'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.capitalize() + '.')

describe_pet('hamster', 'harry')
describe_pet('dog', 'thor')

print('\nARGUMENTOS NOMEADOS')
#Descrevemos o que é cada coisa ao chamar a função, por isso não há a preocupação de inverter parâmetros
def describe_pet(animal_type, pet_name):
    '''Exibe informações sobre um animal de estimação'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.capitalize() + '.')

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

print('\nVALORES DEFAULT')
#Pre-estabelecemos um valor dentro da função já, e se a caso o usuário não informar nada, o valor default será apresentado
def describe_pet(pet_name, animal_type='dog'):
    '''Exibe informações sobre um animal de estimação'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.capitalize() + '.')

describe_pet(pet_name='willie')
describe_pet('willie')      #Como já temos um default só inserimos o dados que queremos apresentar.
describe_pet(pet_name='thor',animal_type='hamster')

print('\nCHAMADAS DE FUNÇÃO EQUIVALENTE')
#Todas as chamadas a seguir serão adequadas a essa função:
#Um cachorro chamado Willie
describe_pet('willie')
describe_pet(pet_name='willie')

#Um hamster chamado Harry
describe_pet('harry','hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
print()

#EXERCICIO
'''
Escreva uma função chamada make_shirt() que aceite um tamanho e o texto de uma mensagem que devera ser
estampada na camiseta. A função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem estampada.
Chame a função uma vez usando arg. posicionais para criar uma camiseta
Chame a função uma segunda vez usando arg. nomeados.
'''

def make_shirt(tamanho, texto):
    print('O tamanho da camiseta será ' + tamanho + ', e a frase será: ' + texto.capitalize() + '.')

make_shirt('G','a vida é bela')
make_shirt(tamanho='M', texto='Happiness is only real when shared')
print()
'''
Modifique a função make_shirt() de modo que as camisetas sejam grandes por default, com uma mensagem Eu amo Python.
Crie uma camiseta grande e outra média com a mensagem default, e uma camiseta de qualquer tamanho com uma mensagem
diferente.
'''

def make_shirt(texto, tamanho='G'):
    print('O tamanho da camiseta será ' + tamanho + ', e a frase será: ' + texto + '.')

make_shirt(texto='Eu amo Python')
make_shirt(texto='Eu amo Python', tamanho='M')
make_shirt(texto='Eu amo Cobol', tamanho='P')
print()

'''
Escreva uma função chamada describe_city() que aceite o nome de uma cidade e seu país. A função deve exibir uma frase
simples, que como Reykjavik está localizada na Islândia. Forneça um valor default ao parâmetro que representa o país.
Chame sua função para três cidades diferentes em que pelo menos uma delas não esteja no país default.
'''

def describe_city(nome, pais='Islândia'):
    print(nome + ' está localizado no(a) ' + pais + '.')

describe_city('Reykjavik')
describe_city(nome='São Paulo', pais='Brasil')
describe_city(nome='Tokyo', pais='Japão')