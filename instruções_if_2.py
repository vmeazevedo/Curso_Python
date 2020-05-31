#Instruções if
#Instruções if simples
age = 19
if age >= 18:
    print('You are old enough to vote!')

#Instruções if-else
age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to voto yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')

#Sintaxe if-elif-else
age = 12
if age < 4:
    print('Your admision cost is $0.')
elif age < 18:
    print('Your admission cost is $5.')
else:
    print('Your admission costa is $10.')

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print('Your admission cost is $'+ str(price)+ '.')
print(f'Your admission cost is ${str(price)}.')

#Usando vários blocos elif
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print(f'Your admission cost is ${str(price)}.')

#Omitindo o bloco else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print(f'Your admission cost is ${str(price)}.')

#Testando várias condições
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')


'''
5.3 - Cores de alienigenas #1: Supona que um alien acabou de ser atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um valor igual a 'green'
'yellow' ou 'red'.'''
print('\n5.3 - Corres de alienigena #1')
alien_color = 'green'
if alien_color == 'green':
    print('Você acabou de ganhar 5 pontos')

# alien_color = 'green'
# if alien_color == 'green':
#     print('Você acabou de ganhar 5 pontos')
# elif alien_color == 'yellow':
#     print('Você acabou de ganhar 10 pontos')

# print('\n5.4 - Corres de alienigena #2')
# alien_color = input(str('Qual a cor do alien? '))
# if alien_color == 'green':
#     print('Você acabou de ganhar 5 pontos')
# else:
#     print('Você acabou de ganhar 10 pontos')

# print('\n5.5 - Corres de alienigena #3')
# alien_color = input(str('Qual a cor do alien? '))
# if alien_color == 'green':
#     print('Você acabou de ganhar 5 pontos.')
# elif alien_color == 'yellow':
#     print('Você acabou de ganhar 10 pontos.')
# elif alien_color == 'red':
#     print('Você acabou de ganhar 15 pontos.')
# else:
#     print('Opção errada.')

# print('\n5.6 - Estágio da vida')
# age = int(input('Qual a sua idade? '))
# if age < 2:
#     print('Você é um bêbe.')
# elif age == 2 or age < 4:
#     print('Você é uma criança.')
# elif age == 4 or age < 13:
#     print('Você é um garoto.')
# elif age == 13 or age < 20:
#     print('Você é um adolescente.')
# elif age == 20 or age < 65:
#     print('Você é um adulto.')
# elif age >= 65:
#     print('Você é um idoso.')


print('\n5.7 - Fruta favorita')
favorite_fruits = ['maça', 'pera', 'banana']
if 'maça' in favorite_fruits:
    print('Você realmente gosta de maças')
if 'pera' in favorite_fruits:
    print('Você realmente gosta de pera')
if 'banana' in favorite_fruits:
    print('Você realmente gosta de banana')