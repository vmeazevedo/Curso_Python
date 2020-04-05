sal = int(input('Qual o seu salário? '))

if sal >= 1250:
    n_sal = (float(sal) * (10/100))
    print('Seu aumento é de R${} reais.'.format(n_sal))
else:
    n_sal = (float(sal) * (15/100))
    print('Seu aumento é de R${} reais.'.format(n_sal))
