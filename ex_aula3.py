'''
EXERCICIO: Faça um programa que pergunte a idade, o peso e a altura de
uma pessoa e decide se ela está apta a ser do exercito.
Para entrar no exercito é preciso ter mais de 18 anos, pesar mais ou igual
a 60kg e medir mais ou igual a 1.70 metros.
'''

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

#CONDIÇÃO
#>18 /  >=60kg    /   >=1.70m
if idade > 18 and peso >= 60 and altura >= 1.70:
    print('Você está apto!')
elif idade < 18 and peso >= 60 and altura >= 1.70:
    print('Você não está apto!')
elif idade > 18 and peso < 60 and altura >= 1.70:
    print('Você não está apto!')
elif idade > 18 and peso >= 60 and altura < 1.70:
    print('Você não está apto!')
else:
    print('Opção inválida!')

    