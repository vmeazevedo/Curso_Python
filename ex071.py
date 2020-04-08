nome = 'BANCO CEV'
print('='*35)
print(f'{nome:^35}')

while True:
    print('=' * 35)
    valori = input('Que valor você quer sacar? R$')
    try:
        valori = int(valori)
        if valori < 1:
            print('Digite um valor correto, acima de 0.')
        else:
            break
    except ValueError:
        print('Digite um valor correto, de um número natural.')

while True:
    valor = valori
    if valor >= 50:
        conta = valor // 50
        resultado = conta * 50
        valor = valor - resultado
        print(f'Total de {conta} cédulas de R$50')
    if valor >= 20:
        conta = valor // 20
        resultado = conta * 20
        valor = valor - resultado
        print(f'Total de {conta} cédulas de R$20')
    if valor >= 10:
        conta = valor // 10
        resultado = conta * 10
        valor = valor - resultado
        print(f'Total de {conta} cédulas de R$10')
    if valori < 10:
        print(f'Total de {valori} cédulas de R$1')
        break
    elif valor == 0:
        break
    else:
        print(f'Total de {valor} cédulas de R$1')
        break
print('='*35)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')