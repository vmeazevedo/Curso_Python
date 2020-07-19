temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:         #Se eu não tiver nenhum dado registrado
        mai = men = temp[1]     #Peso maior e menor é igual a temp[1]
    else:                       #Se eu tiver algum registro
        if temp[1] > mai:       #Se a entrada for maior que a lista mai
            mai = temp[1]       #A lista mai é igual a entrada
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de',end=' ')
for p in princ:                 #Para cada pessoa na lista principal
    if p[1] == mai:             #Se o peso for o maior
        print(f'[{p[0]}]', end=' ')        #Imprimir o nome dela
print()
print(f'O menor peso foi de {men}Kg. Peso de',end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]',end=' ')
print()