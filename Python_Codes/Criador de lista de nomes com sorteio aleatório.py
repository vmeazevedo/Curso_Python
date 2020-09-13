#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

#Realiza uma lista e sorteia uma ordem aleatória

import random
from random import shuffle

lista = []

print('\nVamos sortear a lista de apresentação:\n ')

def lista_alunos():
    while True:
        aluno = input('Digite o seu nome: ')
        lista.append(aluno)
        shuffle(lista)
        quest = input('Deseja colocar mais um nome? S ou N: ').lower()
        if quest == 's':
            continue
        else:
            return False

lista_alunos()
print('Ordem de apresentação será: {}.'.format(lista))
