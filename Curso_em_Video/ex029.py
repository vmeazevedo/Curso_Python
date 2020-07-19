vel = int(input('Qual a velocidade do carro? '))

if vel >= 81:
    print('Você esta acima do limite de 80Km e foi multado.')
    multa = (float(vel)-80) * 7
    print('O valor é de R${} reais.'.format(multa))
else:
    print('Você é um bom condutor.')