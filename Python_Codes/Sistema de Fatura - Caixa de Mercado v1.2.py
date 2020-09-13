#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

#Variável que irá definir se a compra continua ou não
compra = 's'
#Lista onde será armazenado nossos dados
fatura = []
#Variável que irá somar nossa compra
total = 0

print('Bem vindo ao Mercado XYZ!')

#Enquanto o while for 's' a compra continuará
while compra == 's':
    produto = input('Digite o nome do produto: ' )
    preço = float(input('Digite o preço do produto: ' ))
    #Adição do produto e do preço dentro da lista da fatura
    fatura.append([produto,preço])
    #Soma dos valores
    total += preço
    compra = input('Deseja comprar mais algum produto? S/N? ').lower()

print('A sua lista de produtos é: \n')

#Apresenta a lista da fatura formatada
for x in fatura:
    print(x[0],'-',x[1])

print('O total da sua compra ficou em:',total,'reais.')

print(input('Digite enter para continuar..'))
