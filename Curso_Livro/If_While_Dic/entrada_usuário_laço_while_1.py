# #Como a função input trabalha
message = input('Tell somenthing, and I will repeat it back to you: ')
print(message)

# #Escrevendo prompts claros
name = input('Please enter your name: ')
print('Hello, ' + name + '!')

prompts = 'If you tell us who are, we can personalize the messages you see.'
prompts += '\nWhat is your first name? '
name = input(prompts)
print('\nHello, ' + name + '!')

# #Usando int para aceitar entrada numéricas
age = input('How old are you? ')
print(age)

age = input('How old are you? ')
age = int(age)
if age >= 18:
    print(age)

height = input('How tall are you, in inches? ')
height = int(height)

if height >= 36:
    print('\nYou are tall enough to ride!')
else:
    print('\nYou will be able to ride when you are little older.')

#Operador de módulo
a = 4
b = 3
c = 4%3
print(c)

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o primeiro número: '))
c = a%b
print(c)

number = input('Enter a number, and I will tell you if it is even or odd: ')
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.') 

'''
7.1 - Locação de automóveis: Escreva um programa que pergunte ao usuário qual tipo de carro ele gostaria de alugar.
Mostre uma mensagem sobre esse carro, por exemplo, 'Deixe-me ver se consigo um Subaru para você.' '''
carro = input('Qual carro você gostaria de alugar? ')
print('Deixe me ver se consigo um ' + carro + ' para você.')

'''
7.2 - Lugares em um restaurante: Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo para
jantar. Se a resposta for maior que oito exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso contrário,
informe que sua mesa está pronta.'''
mesa = int(input('Uma mesa para quantas pessoas? '))
if mesa >= 8:
    print('Por gentileza, ainda não temos a mesa, por favor, aguardem aqui.')
else: 
    print('Sigam-me a sua mesa está pronta.')

'''
7.3 - Múltiplos de dez: Peça um número ao usuário e, em seguinda, informe se o numero é multiplo de dez ou não.'''
number = input('Digite um número qualquer: ')
number = int(number)

if number % 10 == 0:
    print('\nO numero ' + str(number) + ' é multiplo de 10.')
else:
    print('\nO numero ' + str(number) + ' não é multiplo de 10.')