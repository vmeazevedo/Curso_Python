val_casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Por quando anos você vai financiar? '))
prest = (val_casa/anos) / 12
print('A sua prestação será de R${:.2f} reais.'.format(prest))
porc = (30/100) * sal
print('Margem de segurança de 30% é de {:.2f}.'.format(porc))

if prest > porc:
    print('Desculpe não é possível realizar o financiamento')
elif prest == porc:
    print('Seu financiamento foi aprovado.')
elif prest < porc:
    print('Seu financiamento foi aprovado.')
