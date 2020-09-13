#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

meses = ('janeiro', 'fevereiro', 'março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
data_nasc = input('Por favor, digite a sua data de nascimento no formato DD-MM-AAAA: ')
indice = int(data_nasc[3:5])-1
mes = meses[indice]
print('Você nasceu no mês de',mes)
