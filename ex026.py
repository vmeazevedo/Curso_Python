#Encontrar se o nome SILVA está no nome de uma pessoa.
frase = str(input('Digite uma frase qualquer: ')).lower()
conte = frase.count('a')
encontre = frase.find('a')+1
ultimo = frase.rfind('a')+1

print('A letra a aparece {} vezes.'.format(conte)) #1
print(encontre)

#2
if encontre >= 0:
    print('A letra a aparece a primeira vez na posição {}.'.format(encontre))
elif encontre == -1:
    print('A letra não apareceu.')

#3
print('A ultima vez que a letra a apareceu foi no digito {}.'.format(ultimo))