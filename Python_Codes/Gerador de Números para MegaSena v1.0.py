#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import random

def megasena():
    jogo = []
    while len(jogo) <6:
        num = random.randint(1,60)
        if num in jogo:
            continue
        else:
            jogo.append(num)
    print(jogo)

print('\nOlá! Seja bem vindo ao gerador aleatório de números para a MegaSena!')
input('Pressione enter para receber a sua sequência de números: \n')
megasena()

valid_i = False
while valid_i == False:
    var = input('\nDeseja receber mais um jogo? S ou N: ').lower()
    if var == 's':
        megasena()
    else:
        print('\nObrigado por utilizar o sistema. Até logo\n')
        break
