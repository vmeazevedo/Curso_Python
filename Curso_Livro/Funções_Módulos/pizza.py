def make_pizza(size, *toppings):
    '''Apresenta a pizza que estamos prestes a preparar.'''
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    for n in toppings:
        print('- ' + n)
