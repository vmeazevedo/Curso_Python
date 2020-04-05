salario = float(input('Digite o seu salário: '))
aumento = salario * (15/100)
novo_sal = salario + aumento
print('Seu novo salario é igual a R${:.2f} reais.'.format(novo_sal))

