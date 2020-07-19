#Soma somente os números pares
s = 0
for c in range(0,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s = s+n     # s+= n
    else:
        pass
print('A soma é {}.'.format(s))
