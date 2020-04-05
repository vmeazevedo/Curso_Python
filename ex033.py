n1 = int(input('Digite o primeiro: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print('O menor numero é o {}.'.format(menor))
print('O maior numero é o {}.'.format(maior))
