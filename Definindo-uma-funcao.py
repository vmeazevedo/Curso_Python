def greet_user():
    '''Exibe uma saudação simples'''
    print('Hello World!')

greet_user()

def greet_user2(username):
    '''Exibe uma saudação simples'''
    print('Hello, ' + username + '!')

greet_user2('Vinícius')

'''Escreva uma função chamada display_message() que mostre uma frase informando a
 todos o que você está aprendendo nesse capítulo. Chame a função e certifique-se de 
 que a mensagem seja exibida corretamente.
'''
def display_message(materia):
    print('Neste capítulo eu estou aprendendo sobre, ' + materia + '!')

display_message('funções')

#EXERCICIO
'''Escreva uma função chamada favorite_book() que aceite um parâmetro tittle. A função
deve exibir uma mensagem como 'Um dos meus livros favoritos é Alice no país das maravilhas.
Chame a função e não se esqueça de incluir o título do livro como argumento na chamada da função.
'''

def favorite_book(livro):
    print('Um dos meus livros favoritos é o, ' + livro.capitalize() + '!')

favorite_book('fundação')