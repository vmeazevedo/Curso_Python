km = int(input('Qual a distância da viagem em Km? '))

if km <= 200:
    passagem = (float(km) * 0.5)
    print('O valor da passagem é de R${} reais.'.format(passagem))
else:
    passagem = (float(km) * 0.45)
    print('O valor da passagem é de R${} reais.'.format(passagem))