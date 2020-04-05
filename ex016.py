from math import ceil
from math import floor

num = float(input('Digite um número real qualquer: '))
inte_up = ceil(num)
inte_do = floor(num)
if num > 6.5:
    print('Seu numero inteiro é {}.'.format(inte_up))
else:
    print('Seu número inteiro é {}.'.format(inte_do))

    