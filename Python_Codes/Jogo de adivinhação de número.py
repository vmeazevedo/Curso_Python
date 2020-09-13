#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

#Jogo de adivinhação v1.0
import random

print('\nOlá! Seja bem-vindo ao jogo de adivinhação.')

cond = True
while cond:
    num = random.randint(0,10)
    usuario = int(input('\nPor gentileza, tente adivinhar o valor que estou pensando de 0 a 10: '))
    if usuario == num:
        print('Parabéns você acertou.')
        again = str(input('\nDeseja jogar novamente? S ou N: ')).lower()
        if again == "s":
            cond = True
        else:
            print('\nObrigado por jogar conosco! Até a próxima!\n')
            cond = False
    else:
        print('\nVocê errou. Tente novamente!')

