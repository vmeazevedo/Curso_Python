peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

valor_imc = (peso / (altura*altura)) * 10000
print('Seu IMC é igual a: ', valor_imc)

if valor_imc < 20.7:
    print('Abaixo do peso')
elif valor_imc >= 20.7 and valor_imc <= 26.4:
    print('No peso normal')
elif valor_imc > 26.4 and valor_imc <= 27.8:
    print('Marginalmente acima do peso')
elif valor_imc >= 27.8 and valor_imc <= 31.1:
    print('Acima do peso ideal')
elif valor_imc > 31.1:
    print('Obeso')
else:
    print('Close')