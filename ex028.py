import random

numero = random.randint(0,5)
usuario = int(input('Tente adivinhar o valor que estou pensando de 0 a 5: '))
if usuario == numero:
    print('Parabéns você acertou.')
else:
    print('Tente novamente.')

