#Valores de retorno
#Devolvendo um valor simples
def get_formatted_name(first_name, last_name):
    '''Devolve um nome completo formatado de modo elegante.'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Deixando um argumento opcional
def get_formatted_name(first_name, middle_name, last_name):
    '''Devolve um nome completo formatado de modo elegante.'''
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Devolvendo um dicionário
def build_person(first_name, last_name):
    '''Devolve um dicionário com informações sobre uma pessoa.'''
    person = {'first':first_name, 'last':last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age = ''):
    '''Devolve um dicionário com informações sobre uma pessoa.'''
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#Usando função com um laço while
# def get_formatted_name(first_name, last_name):
#     '''Devolve um nome completo formatado de modo elegante.'''
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# '''Este é um loop infinito.'''
# while True:
#     print('\nPlease tell me you name:')
#     print('(enter "q" at any time to quit)')
#     f_name = input('First name: ')
#     if f_name == 'q':
#         break
#     l_name = input('Last name: ')
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print('\nHello, ' + formatted_name)

'''
8.6 - Nomes de cidade: Escreva uma função chamada city_country() que aceite o nome de uma cidade e seu país.
A função deve devolver uma string formatada assim: 'Santiago, Chile'.'''
print('\n8.6 - Nomes de cidade')
def city_country(cidade, pais):
    dados = cidade + ', ' + pais
    return dados.title()

informações = city_country('santiago','chile')
informações1 = city_country('buenos aires','argentina')
informações2 = city_country('lima','peru')
print(informações)
print(informações1)
print(informações2)

'''
8.7 - Álbum: Escreva uma função chamada make_album() que construa um dicionario descrevendo um album musical.
A função deve aceitar o nome de um artista e o titulo de um album e deve devolver um dicionario contendo essas duas
informações.
Use a funçao para criar tres dicionarios que representem albuns diferentes. Apresente cada valor devolvido para
mostrar que os dicionarios estão armazenados as informações do album corretamente.'''
print('\n8.7 - Album')
def make_album(artista, titulo, faixa=''):
    album = {'nome':artista, 'album':titulo}
    if faixa:
        album['faixa'] = faixa
    return album

album_info = make_album('iron maiden','brave new world')
album_info1 = make_album('kiss','detroit')
album_info2 = make_album('manowar','metal warriors')
album_info3 = make_album('manowar','blood brother', '5')
print(album_info, album_info1, album_info2)
print(album_info3)

'''
8.8 - Album dos usuários: Comece com o seu programa anterior. Escreva um laço while que permita aos usuarios fornecer o nome
de um artista e o titulo de um album. Depois que tiver essas informações, chame make_album() com as entradas dos usuarios e 
apresente o dicionario criado. Lembre-se de incluir um valor de saida no laço while.'''
print('\n8.8 - Album dos usuarios')
def make_album(artista, titulo, faixa=''):
    album = {'nome':artista, 'album':titulo}
    if faixa:
        album['faixa'] = faixa
    return album

while True:
    print('\nPressiona q a qualquer momento para sair.')
    print('Entre com as informações abaixo:')
    n_artista = input('Qual o nome do artista? ')
    if n_artista == 'q':
        break
    n_titulo = input('Qual o titulo do album? ')
    if n_titulo == 'q':
        break
    n_faixa =  input('Qual o numero de faixas? Caso não houver a info somente pressione enter. ')
    if n_faixa == 'q':
        break
    infos = make_album(n_artista, n_titulo, n_faixa)
    print(infos)

