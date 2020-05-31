#Um exemplo simples
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Testes condicionais
#Verificando a igualdade
car = 'bmw'
car == 'bmw'
if car == 'bmw':
    print('True')
else:
    print('False')

#Verificando a diferença
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies')

#Comparações numéricas
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#Testando várias condições
#Usando and para testar várias condições
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print('True')
else:
    print('False')

#Usando or para testar várias condições
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print('True')
else:
    print('False')

#Verificando se um valor está em uma lista
requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print('True')
else:
    print('False')
if 'pepperoni' in requested_topping:
    print('True')
else:
    print('False')

#Verificando se uma valor não está em uma lista
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ', you can post a respose if you wish.')

'''
5.1 - Testes condicionais: Escreva uma serie de testes condicionais. Exiba uma frase que descreva o teste e o resultado previsto
para cada um. Seu codigo devera ser semelhante a:'''
print('\n5.1 - Testes condicionais')
car = 'subaru'
moto = 'suzuki'
barco = 'yamaha'
avião = 'boeing'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is moto == 'suzuki'? I predict True.")
print(moto == 'suzuki')
print("Is barco == 'yamaha'? I predict True.")
print(barco == 'yamaha')
print("Is avião == 'boeing'? I predict True.")
print(avião == 'boeing')


print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("Is moto == 'honda'? I predict True.")
print(moto == 'honda')
print("Is barco == 'nokia'? I predict True.")
print(barco == 'nokia')
print("Is avião == 'latam'? I predict True.")
print(avião == 'latam')

'''
5.2 - Mais testes condicionais: Você não precisa limitar o número de testes que criar em dez. Se quiser testar mais comparações,
escreva outros testes e acrescente-os. Tenha pelo menos um resultado True e um False para cada um dos casos a seguir:'''
print('\n5.2 - Mais testes condicionais')
texto = 'abc'
if texto == 'abc':
    print(texto == 'abc')
else:
    print(texto != 'abcde')

print()
texto = 'ABC'
if texto == 'ABC'.lower():
    print(texto == 'abc')
else:
    print(texto != 'abcde')

print()
a = 5
b = 4
if a == b or a != b:
    print('True')
else:
    print('False')
if a > b:
    print('True')
else:
    print('False')
if a >= b or a <= b:
    print('True')
else:
    print('False')
if a and b >= 1:
    print('True')
else:
    print('False')

print()
lista = ['5', '6', '7', '10']
if '5' in lista:
    print('O numero 5 esta na lista.')

print()
lista = ['5', '6', '7', '10']
if '4' not in lista:
    print('O numero 4 não esta na lista.')

    
