#Percorrendo um dicionário com um laço
#Percorrendo todos os pares chave-valor com um laço
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

print()
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

#Percorrendo todas as chaves de um dicionário com um laço
print()
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages:
    print(name.title())

print()
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print('  Hi '+ name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '.')

print()
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages:
    print('Erin, please take our poll!')

#Percorrendo as chaves de um dicionário em ordem alfabetica usando um laço
print()
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages):
    print(name.title() + ', thank you for taking the poll.')

#Percorrendo todos os valores de um dicionario com um laço
print()
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print('The following languages have been mentioned: ')
for language in favorite_languages.values():
    print(language.title())

#Removendo valores duplicados de um dicionario usando set() no laço
print()
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print('The following languages have been mentioned: ')
for language in set(favorite_languages.values()):
    print(language.title())

'''
6.4 - Glossário 2: Agora que você já sabe como percorrer um dicionário com um laço, limpe o codigo do exercicio 6.3, substituindo sua sequencia
de instruções print por um laço que percorra as chaves e os valores do dicionario. Quando tiver certeza que seu laço funciona, acrescente mais cinco
termos de Python ao seu glossario. Ao executar seu programa novamente, essas palavras e significados novos deverão ser automaticamente incluidos na saida.'''
print('\n6.4 - Glossário 2')
dic = {
    'palavra_1':'a',
    'significa_1':'a primeira letra do alfabeto', 
    'palavra_2':'b',
    'significa_2':'a segunda letra do alfabeto', 
    'palavra_3':'c',
    'significa_3':'a terceira letra do alfabeto', 
    'palavra_4':'d',
    'significa_4':'a quarta letra do alfabeto', 
    'palavra_5':'e',
    'significa_5':'a quinta letra do alfabeto',
    }
for chave, valor in dic.items():
    print(chave.title() + ': ' + valor.capitalize())


'''
6.5 - Rios: Crie um dicionário que contenha três rios importantes e o pais que cada rio corta. Um par chave-valor poder ser 'nilo':'egito'.'''
print('\n6.5 - Rios')
rios = {
    'nilo':'egito',
    'amazonas':'brasil',
    'negro':'brasil',
}
for c,v in rios.items():
    print('O ' + c.title() + ' corre pelo ' + v.title() + '.')

print('\nOs nomes dos rios são:')
for chave in rios:
    print(chave.title())

print('\nOs nomes dos países são:')
for valor in rios.values():
    print(valor.title())

'''
6.6 - Enquete: Utileze o codigo da pag 150.'''
print('\n6.6 - Enquete')
list = ['jen','sarah','edward','phil','pedro','roberto']

favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in list:
    if name in favorite_languages:
        print('Muito obrigado ' + str(name).title() + ' por responder a pesquisa.')
    if name not in favorite_languages:
        print('Por gentileza ' + str(name).title() + ' poderia responder a pesquisa?')