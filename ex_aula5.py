'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que serão 
convidadade para uma festa.
O programa irá perguntar o nome de todas as pessoas e colocar
em uma lista de convidados, e após isso irá imprimir todos os nomes da lista
'''

lista_nomes = []

cont = 0
while True:
    cont += 1
    nomes = str(input('Qual o nome de quem vira? '))
    lista_nomes.append(nomes)
    resp = str(input('Deseja acrescentar outro nome? [S/N]: '))
    if resp == 's':
        continue
    else:
        break
print('A lista de convidados é:')
print(lista_nomes)
