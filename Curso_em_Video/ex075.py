vezes = 0
pares = []

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

if n1 == 9:
    vezes +=1
if n2 == 9:
    vezes +=1
if n3 == 9:
    vezes +=1
if n4 == 9:
    vezes +=1


print(f'Você digitou os valores ({n1},{n2},{n3},{n4})')
print(f'O valor 9 apareceu {vezes} vezes.')
if n1 == 3:
    print('O valor 3 apareceu na 1ª posição.')
elif n2 == 3:
    print('O valor 3 apareceu na 2ª posição.')
elif n3 == 3:
    print('O valor 3 apareceu na 3ª posição.')
elif n4 == 3:
    print('O valor 3 apareceu na 4ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

if n1 % 2 == 0:
    pares.append(n1)
if n2 % 2 == 0:
    pares.append(n2)
if n1 % 2 == 0:
    pares.append(n3)
if n2 % 2 == 0:
    pares.append(n4)    
print('Os valores pares digitados foram ',pares)
    