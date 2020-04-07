import random

vezes = 0
numero = random.randint(0,10)
usuario = int(input('Tente adivinhar o valor que estou pensando de 0 a 5: '))

while numero != usuario:
    print('Você errou, tente novamente.')
    usuario = int(input('Tente adivinhar o valor que estou pensando de 0 a 5: '))
    vezes = vezes + 1
    if usuario == numero:
        print('Parabéns!')

print('\nO número de tentativas que você fez até acertar foi {}.'.format(vezes))