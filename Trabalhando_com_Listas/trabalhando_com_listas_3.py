#Trabalhando com parte de lista
#Fatiando uma lista
players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

#Se omitirmos o primeiro indice começamos automaticamente do indice 0
players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

#Se omitirmos o ultimo indice o preenchimento será do indice que indicarmos até o final
players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

#Apresentar os 3 ultimos indices
players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#Percorrendo uma fatia com um laço
players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#Copiando uma lista
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print('My favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friends_foods)


print()
players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#Copiando uma lista
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print('My favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friends_foods)


'''
4.10 - Fatias: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:'''
print('4.10 - Fatias')
comidas = ['pizza', 'falafel', 'cenoura', 'carne', 'tomate', 'macarrão']
print('Os três primeiros itens são: ')
for n in comidas[:3]:
    print(n.title())
print('Os três itens do meio da lista sao: ')
for n in comidas[2:4]:
    print(n.title())
print('Os três ultimos itens da lista são: ')
for n in comidas[-3:]:
    print(n.title())

'''
4.11 - Minhas pizzas, suas pizzas: Comece com seu programa do Exer 4.1. Faça uma cópia da lista de pizzas e chame-a de friend_pizzas. 
Então faça o seguinte:'''
print()
print('4.1 - Pizzas')
pizzas = ['mussarela', 'margarita', 'frango']
friend_pizzas = pizzas[:]

pizzas.append('jaba')
friend_pizzas.append('catupiry')

print('Minhas pizzas favoritas são: ')
for n in pizzas:
    print(n.title())

print('\nAs pizzas favoritas dos meus amigos sãos: ')
for n in friend_pizzas:
    print(n.title())
