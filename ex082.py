lista = []
lista2 = []
lista3 = []

while True:
    entrada = int(input('Digite um valor: '))
    lista.append(entrada)
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta == 's':
        continue
    else:
        break

print(f'A lista completa é {lista}')
for valor in lista:
    if valor % 2 == 0:
        lista2.append(valor)
    else:
        lista3.append(valor)
print(f'A lista de pares é {lista2}')
print(f'A lista de ímpares é {lista3}')
