lista = []

while True:
    entrada = int(input('Digite um valor: '))
    lista.append(entrada)
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta == 's':
        continue
    else:
        break
    
print('-='*25)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(F'Você digitou os valores {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')