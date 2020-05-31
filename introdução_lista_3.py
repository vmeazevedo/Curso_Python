#Organizando uma lista
#Ordenando uma lista de forma permanente com o método sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Ordenando uma lista ao contrário
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Ordenando uma lista temporariamente com a função sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list: ')
print(cars)

print('\nHere is the sorted list: ')
print(sorted(cars))

print('\nHere is the original list again: ')
print(cars)

#Exibindo uma lista em ordem inversa
print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Descobrindo o tamanho de uma lista~
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


'''
3.8 - Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de visitar.'''
print('3.8 - Conhecendo o mundo')
mundo = ['portugal', 'canada', 'eua', 'japão', 'espanha']
print(mundo)
print(sorted(mundo))
print(mundo)
print(sorted(mundo, reverse=True))
print(mundo)
mundo.reverse()
print(mundo)
mundo.reverse()
print(mundo)
mundo.sort()
print(mundo)
mundo.sort(reverse = True)
print(mundo)
