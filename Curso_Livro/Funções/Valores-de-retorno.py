#DESENVOLVENDO UM VALOR SIMPLES
def get_formatted_name(first_name, last_name):
    '''Devolve um nome completo formatado de modo elegante.'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#DEIXANDO UM ARGUMENTO OPCIONAL
def get_formatted_name(first_name, middle_name, last_name):
    '''Devolve um nome completo formatado de modo elegante.'''
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    '''Devolve um nome completo formatado de modo elegante.'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician1 = get_formatted_name('jimi','hendrix')
print(musician1)

musician2 = get_formatted_name('jimi','hooker','lee')
print(musician2)


#DEVOLVENDO UM DICIONARIO
def build_person(first_name,last_name):
    '''Devolve um dicionário com informações sobre uma pessoa.'''
    person = {'first':first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age = ''):
    '''Devolve um dicionário com informações sobre uma pessoa.'''
    person = {'first':first_name, 'last': last_name}
    if age:                                                  #Significa se o AGE for True, ou seja tiver um valor.
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)


#USANDO UMA FUNÇÃO COM UM LAÇO WHILE
def get_formatted_name(first_name, last_name):
    '''Devolve um nome completo formatado de modo elegante.'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

#Este é um loop infinito!
while True:
    print('\nPlease tell me your name: ')
    print("(enter 'q' at any time to quit)")
    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print('\nHello, ' + formatted_name + "!")

#EXERCICIOS

'''
Escreva uma função chamada city_country() que aceite o nome de uma cidade e seu país.
A função deve devolver uma string formatada assim: 'Santiago, Chile'
Chame sua função com pelo menos três pares cidade-país e apresente o valore devolvido.
'''
def city_country(cidade, pais):
    nome_formatado = cidade + ', ' + pais
    return nome_formatado.title()

var = city_country('santigo','chile')
var2 = city_country('lima','peru')
var3 = city_country('buenos aires','argentina')
print(var)
print(var2)
print(var3)

'''
Escreva uma função chamada make_album() que construa um dicionário descrevendo um álbum musical.
A função deve aceitar o nome de um artista e o título de um álbum e deve devolver um dicionário contendo
essas duas informações. Use a função para criar três dicionários que representem álbuns diferentes.
Apresente cada valor devolvido para mostrar que os dicionários estão armazenando as informações do album corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar o número de faixas em um album. Se a linha
que fizer a chamada incluir um valor para o número de faixas, acrescente esse valor ao dicionário do album. Faça pelo menos
uma nova chamada da função incluindo o número de faixas em um album.
'''
def make_album(artista, album,faixas=''):
    info = {'Nome Artista': artista, 'Título Álbum': album}
    if faixas:
        info['Nº Faixas'] = faixas
    return info

info1 = make_album('Jimi Hendrix','ABC')
info2 = make_album('Iron Maiden','Powerslave')
info3 = make_album('Kiss','Detroit Rock City')
info4 = make_album('Motorhead', 'Ace of Spades', faixas = 12)
print(info1)
print(info2)
print(info3)
print(info4)

'''
Comece com o seu programa do Exercicio 8.7. Escreva um laço while que permita aos usuários fornecer o nome de um artista e o título de um álbum.
Depois que tiver essas informações, chame make_album() com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um valor
de saída no laço while.
'''
def make_album(artista, album):
    info = {'Nome Artista': artista, 'Título Álbum': album}
    return info

while True:
    print('Por gentileza informe o artista e o álbum ou N para sair.')
    artista = input('Artista: ')
    if artista == 'N':
        break
    album = input('Álbum: ')
    if album == 'N':
        break

    formatado = make_album(artista,album)
    print(formatado)
    print()














