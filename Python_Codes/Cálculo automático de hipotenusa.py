#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import math

#Cálculo automatico de hipotenusa
cat_1 = int(input('Digite o cateto adjacente: '))
cat_2 = int(input('Digite o cateto oposto: '))
hipo = math.hypot(cat_1,cat_2)
print('A sua hipotenusa é {:.2f}.'.format(hipo))
