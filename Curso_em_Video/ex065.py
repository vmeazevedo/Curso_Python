import random

vezes = []
usuario = ''

while usuario != 0:
    usuario = int(input('Digite um número: '))
    vezes.append(usuario)
    resposta = str(input('Você gostaria de digitar um outro número? [S/N]: ')).lower()
    if resposta == 's':
        continue
    else:
        break

soma = sum(vezes)
print(soma)

qto_num = len(vezes)

media = soma /qto_num
print('A média dos números digitados é {}.'.format(media))

vezes.sort()
print('O menor valor é {} e o maior é o {}.'.format(vezes[0],vezes[-1]))




