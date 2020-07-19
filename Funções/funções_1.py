#Definindo uma função
def great_user():
    '''Exibe uma saudação simples.'''
    print('Hello!')
great_user()

#Passando informação para uma função
def great_user(username):
    '''Exibe uma saudação simples.'''
    print('Hello ' + username.title() + '!')
username = input('Qual o seu nome? ')
great_user(username)                        #Chamando a função utilizando uma variavel e dados de input
great_user('jesse')                         #Outra forma de chamar a função

''' 
8.1 - Mensagem: Escreva uma função chamada display_message(), que mostre uma frase informando a todos o que
você esta aprendendo neste capítulo. Chame a função e certifique-se de que a mensagem seja exibida corretamente.'''
print('\n8.1 - Mensagem')
def display_message():
    print('Neste capítulo eu estou aprendendo sobre funções.')
display_message()

'''
8.2 - Livro favorito: Escreva uma função chamada favorite_book() que aceite um parâmetro title. A função deve exibir
uma mensagem como Um dos meus livros favoritos é Alice no país das maravilhas. Chame a função e não se esqueça de incluir
o titulo do livro como argumento na chamada da função.'''
print('\n8.2 - Livro favorito')
def favorite_book(book):
    print('Um dos meus livros favoritos é ' + book.title() + '!')
livro = input('Qual um dos seus livros favoritos? ')
favorite_book(livro)
