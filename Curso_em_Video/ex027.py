#mostrar somente o primeiro e o ultimo nome
nome = str(input('Digite o seu nome completo: '))
dividido = nome.split()
print('Seu nome completo é: ',nome)
print('O seu primeiro nome é {} e o ultimo é {}.'.format(dividido[0],dividido[-1]))