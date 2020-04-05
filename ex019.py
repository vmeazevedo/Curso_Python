import random

a1 = input('Digite o seu nome: ')
a2 = input('Digite o seu nome: ')
a3 = input('Digite o seu nome: ')

sort = random.randint(1,3)

if sort == 1:
    print('O selecionado foi, {}.'.format(a1))
elif sort == 2:
    print('O selecionado foi, {}.'.format(a2))
elif sort == 3:
    print('O selecionado foi, {}.'.format(a3))
else: 
    ()