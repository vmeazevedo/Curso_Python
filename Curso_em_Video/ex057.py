resposta = str(input('Digite o seu sexo [M/F]: ')).upper()
while resposta != 'M' and resposta != 'F':
    print('Você não digitou M ou F.')
    resposta = str(input('Digite o seu sexo [M/F]: ')).upper()
print('O seu sexo é {}.'.format(resposta))