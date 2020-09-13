#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

#Conversor de angulo para coseno/seno.

import math

ang = float(input('Digite um angulo qualquer para converter: '))
cos = math.cos(ang)
sen = math.sin(ang)
print('O seu coseno é {:.5f} e o seu seno é {:.5f}.'.format(cos,sen))
