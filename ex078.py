valores = []

for cont in range(0,5):
    valores.append(int(input('Digite um valor para a Posição: ')))
print('=-'*25)
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')
for chave, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{chave}',end = ' ')
print()

print(f'O menor valor digitado foi {min(valores)} nas posições',end=' ')
for chave, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{chave}',end = ' ')
print()

