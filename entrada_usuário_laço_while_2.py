#Introdução aos laços while
#Laços while em ação
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number +=1

# #Deixando o usuário decidir quando quer sair
# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += '\nEnter "quit" to end the program. '

# message = ''
# while message != 'quit':
#     message = input(prompt)
    
#     if message != 'quit':
#         print(message)

# #Usando uma flag
# print('\nUsando uma flag no while.')
# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# #Usando break para sair de um laço
# prompt = '\nPlease enter the name of a city you have visited:'
# prompt += '\n(Enter "quit" when you are finished.)'

# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print('I would love to go to ' + city.title() + '!')

#Usando continue em um laço
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)