maior = []
menor = []
atual = 2020

for c in range(0,8):
    ano = input('Digite o ano do seu nascimento: ')
    if ano <= '2002':
        maior.append(ano)
        maior.sort()
    elif ano > '2002':
        menor.append(ano)
        menor.sort()
print('Os que disseram esses anos de nascimento já são de maior:\n {}.'.format(maior))

print('Os que disseram esses anos de nascimento ainda são de menor:\n {}.'.format(menor))
