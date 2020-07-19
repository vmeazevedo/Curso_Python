s = 0
for a in range(1, 500, 2):
    if a % 3 == 0: #O restante deve ser igual a zero quando esse número é dividido por 3
        s += a
print('Soma:', s)
print('FIM')