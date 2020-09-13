#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

#Separador de número por milhar, centena, dezena e unidade
num = str(input('Entre com um número de 0 a 9999: '))

print('\nAnalizando o número {}'.format(num)) 
print('\nUnidade: {}'
    '\nDezena: {}'
    '\nCentena: {}'
    '\nMilhar: {}'
    .format(num[3], num[2], num[1], num[0]) 
      )


