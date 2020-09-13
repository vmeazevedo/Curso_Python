#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

print('Seja bem vindo ao sistema de calculo de média ponderada.')
nota1 = float (input('Digite a nota 1: '))
peso1 = int (input('Digite o peso 1: '))
nota2 = float (input('Digite a nota 2: '))
peso2 = int (input('Digite o peso 2: '))
media_p = (nota1*peso1 + nota2*peso2) / (peso1+peso2)
print('Sua média pondera é:', media_p)
