vezes = []
usuario = ''

while usuario != 999:
    usuario = int(input('Digite um número: '))
    vezes.append(usuario)
    if usuario == 999:
        print('\nVocê digitou 999 que corresponde a sair do programa.')
        print('\nAté logo!')

qto_num = len(vezes)-1
print('A quantidade de números que foi digitado é {}.'.format(qto_num))

soma = sum(vezes)-999
print('A soma entre os valores digitado é {}.'.format(soma))