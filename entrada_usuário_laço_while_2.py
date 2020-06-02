#Introdução aos laços while
#Laços while em ação
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1

# #Deixando o usuário decidir quando quer sair
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter "quit" to end the program. '

message = ''
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)

# #Usando uma flag
print('\nUsando uma flag no while.')
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# #Usando break para sair de um laço
prompt = '\nPlease enter the name of a city you have visited:'
prompt += '\n(Enter "quit" when you are finished.)'

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print('I would love to go to ' + city.title() + '!')

#Usando continue em um laço
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#Evitando loops infinitos
print()
x = 1
while x <= 5:
    print(x)
    x +=1

'''
7.4 - Ingredientes para uma pizza: Escreva um laço que peça ao usuário para fornecer uma serie de ingredientes para uma pizza
até que o valor 'quit' seja fornecido. A medida que cada ingrediente é especificado, apresente uma mensagem informando que você
acrescentará esse ingrediente a pizza.'''
print('\n7.4 - Ingredientes para uma pizza')
texto = 'Informe os ingrediente que iremos usar na pizza, ao final digite "quit" para sair.'
while True:
    ingrediente = input('Me diga qual ingrediente utilizaremos na pizza: ')
    if ingrediente == 'quit':
        print('Até logo!')
        break
    elif ingrediente != 'quit':
        print(ingrediente.title() + ' foi adicionado a pizza!')

'''
7.5 - Ingressos para o cinema: Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa.
Se uma pessoa tiver menos de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 a 12 anos, o ingresso custará
10 dolares, se tiver mais de 12 anos, o ingresso custará 15 dolares. Escreva um laço em que você pergunte a idade aos 
usuários e, então, informe-lhes o preço do ingresso do cinema.'''
print('\n7.5 - Ingressos para o cinema')
while True:
    question = int(input('Por gentileza qual a sua idade? '))
    if question < 3:
        print('O seu ingresso é gratuito!')
        break
    elif question == 3 or question < 12:
        print('O seu ingresso custa 10 dolares.') 
        break
    elif question > 12:
        print('O seu ingresso custará 15 dolares.')
        break

''' 
7.6 - Três saídas: Escreva versões diferentes do ex. 7.4 e 7.5 que faça o seguinte, pelo menos uma vez:'''
#Já realizado

'''
7.7 - Infinito: Escreva um laço que nunca termine e execute-o.'''
x = 1111111111111111111111111111111
while x > 5:
    print(x)