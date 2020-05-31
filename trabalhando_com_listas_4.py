#Tuplas
#Definindo uma tupla
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Percorrendo todos os valores de uma tupla com um laço
print()
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#Sobrescrevendo uma tupla
print()
dimensions = (200, 50)
print('Original dimensions: ')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions: ')
for dimension in dimensions:
    print(dimension)

'''
4.13 - Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco pratos
simples e armazene-os em uma tupla.'''
pratos_simples = ('arroz', 'feijão', 'carne', 'salada', 'suco')
print('As opções de pratos da casa são: ')
for n in pratos_simples:
    print(n.title())
print()
pratos_simples = ('macarrão','feijoada','cannoli','empadão')
print('O nosso cardapio mudou, confira o novo cardapio: ')
for n in pratos_simples:
    print(n.title())

