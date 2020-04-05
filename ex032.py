ano = int(input('Digite um ano em AAAA para saber se ele é bissexto: '))

if (ano%4) == 0:
    print('Ele é bissexto.')
else:
    print('Ele não é bissexto.')