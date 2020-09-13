'''
EXERCICIO: Faça um formulario que pergunte o nome, cpf, endereço
idade, altura e telefone e imprima em um relatório organizado.
'''

print('Olá por gentileza, eu gostaria de solicitar algumas coisas.')
nome = str(input('Qual o seu nome? '))
cpf = int(input('Qual o seu CPF? '))
end = str(input('Qual o seu endereço? '))
idade = int(input('Qual a sua idade? '))
alt = float(input('Qual a sua altura? '))
tel = int(input('Qual o seu telefone? '))

print('A relação dos dados é:')
print('Nome: ',nome)
print('CPF: ',cpf)
print('Endereço: ',end)
print('Idade: ',idade)
print('Altura: ',alt)
print('Telefone: ',tel)
