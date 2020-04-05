import math

cat_1 = int(input('Digite o primeiro cateto: '))
cat_2 = int(input('Digite o primeiro cateto: '))
hipo = math.hypot(cat_1,cat_2)
print('A sua hipotenusa é {:.2f}.'.format(hipo))
