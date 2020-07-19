litro_1 = 2


largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / litro_1

print('Sua area é equivalente a {} metros quadrados.'.format(area))
print('E irá precisar de {} litros de tinta.'.format(tinta))


