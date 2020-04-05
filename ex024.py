
#Verificar se a primeira palavra começa com SANTO
cidade = str(input('Digite o nome da sua cidade: ')).lower()
encontre = cidade.find('santo')
print(encontre)
if encontre == 0:
    print('Começa.')
else:
    print('Não começa.')