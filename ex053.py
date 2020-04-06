fra = str(input('Digite uma frase: '))
fra = fra.replace(' ','')   #retira os espaços
ifra = fra[::-1]    #inverte uma string

print('O inverso de {} é {}.'.format(fra,ifra))
if fra == ifra:
    print('A frase é um palindromo.')
else:
    print('A frase não é um palindromo.')