#Identificador de números primos
a = int(input('Digite um número: '))
if a % 3 == 0 and a % a == 0: 
    print('Ele é um número primo.')
else:
    print('Ele não é um número primo.')

