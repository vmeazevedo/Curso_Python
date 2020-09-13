#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

from random import randint
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0,2)

perguntar = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POOH!!!\n")

print("-="*20)
print("O computador escolheu: {}".format(lista[computador]))
print("O jogador escolheu: {}".format(lista[perguntar]))
print("-="*20)

if computador == 0:
    if perguntar == 0:
        print("Empate!")
    elif perguntar == 1:
        print("Jogador perdeu")
    elif perguntar == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1:
    if perguntar == 0:
        print("Computador perdeu")
    elif perguntar == 1:
        print("Empate!")
    elif perguntar == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    if perguntar == 0:
        print("Jogador venceu")
    elif perguntar == 1:
        print("Computador venceu")
    elif perguntar == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")
