peso = []

for c in range(0,5):
    kg = int(input('Digite o seu peso: '))
    peso.append(kg)
    peso.sort()

print('O menor peso é {} e o maior peso é {}.'.format(peso[0],peso[-1]))