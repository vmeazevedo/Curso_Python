#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

# Formula de baskara #

# Inserir o numero de x²
a = int(input('Insira o numero de X²:'))
# Inserir o numero de x
b = int(input('Insira o numero de X:'))
# Inserir o numero de 
c = int(input('Insira o numero:'))

#Espaçamento entre input e output
print('\n')

# Calculo do valor de Delta
delta = (b**2) - (4*a*c)
print('Delta é igual a:', delta)

# Calculo do valor de X1
x1 = ((-b) + (delta ** 0.5)) / (2*a)
print('Valor de X1 é:', x1)

# Calculo do valor de X2
x2 = ((-b) - (delta ** 0.5)) / (2*a)
print('Valor de X2 é:', x2)
