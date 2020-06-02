# #Como a função input trabalha
# message = input('Tell somenthing, and I will repeat it back to you: ')
# print(message)

# #Escrevendo prompts claros
# name = input('Please enter your name: ')
# print('Hello, ' + name + '!')

# prompts = 'If you tell us who are, we can personalize the messages you see.'
# prompts += '\nWhat is your first name? '
# name = input(prompts)
# print('\nHello, ' + name + '!')

# #Usando int para aceitar entrada numéricas
# age = input('How old are you? ')
# print(age)

# age = input('How old are you? ')
# age = int(age)
# if age >= 18:
#     print(age)

# height = input('How tall are you, in inches? ')
# height = int(height)

# if height >= 36:
#     print('\nYou are tall enough to ride!')
# else:
#     print('\nYou will be able to ride when you are little older.')

#Operador de módulo
# a = 4
# b = 3
# c = 4%3
# print(c)

# a = int(input('Digite o primeiro número: '))
# b = int(input('Digite o primeiro número: '))
# c = a%b
# print(c)

number = input('Enter a number, and I will tell you if it is even or odd: ')
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.') 
    