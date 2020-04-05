
#Encontrar se o nome SILVA está no nome de uma pessoa.
nome = str(input('Digite o seu nome: ')).lower()
encontre = nome.find('silva')
print(encontre)
if encontre != -1:
    print('Tem.')
else:
    print('Não Tem.')