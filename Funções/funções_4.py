#Passando uma lista para uma função
def greet_users(names):
    '''Exibe uma saudação simples a cada usuário da lista.'''
    for name in names:
        msg = 'Hello ' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#Modificando uma lista em uma função
print()
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()            #Retira o ultimo da lista e coloca na variavel current
        print('Printing model: ' + current_design.title())          #Mostra o valor da variavel
        completed_models.append(current_design)             #Add o valor da variavell na lista completed_models

def show_completed_models(completed_models):
    print('\nThe following models have been printed: ')
    for n in completed_models:                              #Para cada item da lista, será apresentado ele
        print(n.title())

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#Evitando que uma função modifique uma lista
print()
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()            #Retira o ultimo da lista e coloca na variavel current
        print('Printing model: ' + current_design.title())          #Mostra o valor da variavel
        completed_models.append(current_design)             #Add o valor da variavell na lista completed_models

def show_completed_models(completed_models):
    print('\nThe following models have been printed: ')
    for n in completed_models:                              #Para cada item da lista, será apresentado ele
        print(n.title())

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)        #Colocamos [:] para criar uma copia da lista unprinted, mantendo a original intacta
show_completed_models(completed_models)
print(unprinted_designs)                                    #Validando que a lista não foi alterada

'''
8.9 - Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma função chamada show_magicians() que exiba o nome de cada mágico da lista.'''
print('\n8.9 - Mágicos')
def show_magicians(nome):
    for n in nomes_magicos:
        print(n.title())

nomes_magicos = ['magico_1','magico_2','magico_3']
show_magicians(nomes_magicos)

'''
8.10 - Grandes mágicos: Comece com uma cópía de seu programa anterior. Escreva uma função chamada make_great() que modifique a lista de magicos
acrescentando a expressão o Grande ao nome de cada magico. Chame show_magicians() para ver a lista foi realmente modificada.'''
print('\n8.10 - Grandes mágicos')
def make_great(nome_magicos, var):
    while nomes_magicos:
        magico_atual = nomes_magicos.pop() + ' o Grande.'
        var.append(magico_atual)
        
def show_magicians(nomes_magicos):
    for n in nomes_magicos:
        print(n.title())

nomes_magicos = ['magico_1','magico_2','magico_3']
var = []

print('Lista 1: ' + str(nomes_magicos))
print('Lista 2: ' + str(var))

make_great(nomes_magicos, var)
nomes_magicos = var
show_magicians(nomes_magicos)

print('Lista 1: ' + str(nomes_magicos))
print('Lista 2: ' + str(var))

'''
8.11 - Magicos inalterados: Comece com o trabalho feito anteriormente. Chame a função make_great com uma copia da lista de nomes de magicos.
Como a lista original nao será alterada, devolve a nova lista e armazene-a em uma lista separada. Chame show_magicians() com cada lista para mostrar que voce tem uma lista
de nomes originais e uma lista com a expressão o Grande add ao nome de cada magico.'''