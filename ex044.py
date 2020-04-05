prod = float(input('Digite o valor do produto: '))
adc = (10/100) * prod
ac = (5/100) * prod
p2x = prod
p2x = (20/100) * prod


print('Menu de opções:')
print('1. A vista - Dinheiro')
print('2. A vista - Cartão')
print('3. Parcelado - 2x')
print('4. Parcelado - 3x ou mais')

entrada = int(input('Digite a opção selecionada: '))

if entrada == 1:
    print('Você receberá um descoto nessa compra de R${:.2f} reais.'.format(adc))
    print('O total da compra será R${:.2f} reais.'.format(prod-adc))
elif entrada == 2:
    print('Você receberá um descoto nessa compra de R${:.2f} reais.'.format(ac))
    print('O total da compra será R${:.2f} reais.'.format(prod-ac))
elif entrada == 3:
    print('Para essa operação não disponibilizamos desconto.')
    print('O total da compra será R${:.2f} reais, parcelado em até 2x.'.format(prod))
elif entrada == 4:
    print('Você receberá um descoto nessa compra de R${:.2f} reais.'.format(p2x))
    print('O total da compra será R${:.2f} reais, parcelado em 3x ou mais.'.format(prod-p2x))