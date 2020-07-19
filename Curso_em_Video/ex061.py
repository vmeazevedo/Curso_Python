print('='*40)
print('Cálculo de PA')
print('='*40)

c_razao = int(input('Digite a razão: '))
f_term = int(input('Digite o term: '))

pa = 0

while pa < 10:
    print(f_term)
    f_term = c_razao + f_term
    pa = pa +1

