#Percorrendo uma lista com um laço
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#Executando mais tarefas em um laço for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')

print()
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next tricky, " + magician.title() + ".\n")


print()
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next tricky, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

'''
4.1 - Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os nomes dessas 
pizzas e, então utilize um laço for para exibir o nome de cada pizza.'''
print()
print('4.1 - Pizzas')
pizzas = ['mussarela', 'margarita', 'frango']
for n in pizzas:
    print(n.title())
    print('Gosto de pizza de ' + n + '.')

print('Essa pizza de ' + pizzas[0].title() + ' está otima! Eu realmente adoro pizza.')
print('Essa pizza de ' + pizzas[1].title() + ' está otima! Eu realmente adoro pizza.')
print('Essa pizza de ' + pizzas[2].title() + ' está otima! Eu realmente adoro pizza.')

'''
4.2 - Animais: Pense em pelo menos três animais diferentes que tenham uma caracteristica
em comum. Armazene os nomes desses animais em uma lista e, então, utilize um laço for para
exibir o nome de cada animal.'''
animal = ['thor', 'rufus', 'mike']
for a in animal:
    print(a.title())
    print('O ' + a.title() + ' é um bom cachorro.')
    print('Um cachorro sem dúvida é o melhor amigo do homem!')