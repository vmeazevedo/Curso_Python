total = 0
tem_mil = 0
menor = 0
contador = 0
barato = ''


while True:
    print('-'*15)
    print('LOJA SUPER BARATÃO')
    print('-'*15)

    produto = str(input('Nome do produto: '))
    
    dindin = float(input('Preço: '))
    contador = contador +1
    total = total+dindin

    if contador == 1 or dindin < menor:
        menor = dindin
        barato = produto

    if dindin > 1000:
        tem_mil = tem_mil+1

    cont = ' '
    while cont not in 'sn':
        cont = str(input('\nQuer continuar? [S/N]: ')).lower()
    if cont == 'n':
        break

print(f'\nO total da compra foi R${total:.2f}.')
print(f'Temos {tem_mil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')