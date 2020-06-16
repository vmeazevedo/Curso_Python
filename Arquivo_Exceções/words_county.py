def count_words(filename):
    '''Conta o número aproximado de palavras em um arquivo.'''
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' doest not exist.'
        print(msg)
    else:
        '''Conta o número aproximado de palavras no arquivo.'''
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

filenames = 'Arquivo_Exceções\\alice.txt', 'Arquivo_Exceções\\siddharta.txt', 'Arquivo_Exceções\\moby_dick.txt', 'Arquivo_Exceções\\litte_women.txt'
for n in filenames:
    count_words(n)


#Falhando silenciosamente
print()
def count_words(filename):
    '''Conta o número aproximado de palavras em um arquivo.'''
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        '''Conta o número aproximado de palavras no arquivo.'''
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

filenames = 'Arquivo_Exceções\\alice.txt', 'Arquivo_Exceções\\siddharta.txt', 'Arquivo_Exceções\\moby_dick.txt', 'Arquivo_Exceções\\litte_women.txt'
for n in filenames:
    count_words(n)
    
#Salvando erros em um arquivo
print()
def count_words(filename):
    '''Conta o número aproximado de palavras em um arquivo.'''
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        filename2 = 'Arquivo_Exceções\\missing_files.txt'                               #Criando um arquivo para salvar os erros de arquivos nao encontrados
        with open(filename2,'w') as file_object:                                        #Acessando o arquivo em modo write
            file_object.write('Sorry, the file ' + filename + ' doest not exist.\n')    #Add a o arquivo os arquivos nao encontrados no filename.
    else:
        '''Conta o número aproximado de palavras no arquivo.'''
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

filenames = 'Arquivo_Exceções\\alice.txt', 'Arquivo_Exceções\\siddharta.txt', 'Arquivo_Exceções\\moby_dick.txt', 'Arquivo_Exceções\\litte_women.txt'
for n in filenames:
    count_words(n)

'''
10.6 - Adição: Um problema comum quando pedir entradas numéricas ocorre quando as pessoas fornecem texto no lugar de números.
Ao tentar converter a entrada para uma int, você obterá um TypeError. Escreva um programa que peça dois números ao usuário.
Some-os e mostre o resultado. Capture o TypeError caso algum dos valores de entrada nao seja um numero e apresente uma mensagem
de erro simpatica. Teste seu programa fornecendo dois numeros e, em seguida, digite um texto no lugar de um numero.
'''
# print('\nAdição')
# while True:
#     try:
#         num1 = int(input('Digite o primeiro numero: '))
#         num2 = int(input('Digite o segundo numero: '))
#         soma = num1+num2
#         print(f'O resultado da soma é {soma}.')
#         break
#     except:
#         print('Digite apenas números inteiros e não letras.')

# #Outra solução utilizando flags
# print('\nAdição')
# flag = True
# while flag:
#     try:
#         num1 = int(input('Digite o primeiro numero: '))
#         num2 = int(input('Digite o segundo numero: '))
#         soma = num1+num2
#         print(f'O resultado da soma é {soma}.')
#         flag = False
#     except:
#         print('Digite apenas números inteiros e não letras.')
        
'''
10.7 - Calculadora para adição: Coloque o código anterior em um laço while para que o usuário possa continuar fornecendo numeros,
mesmo se cometerem um erro e digitarem um texto no lugar do numero.'''
# print('\nCalculadora para adição')
# while True:
#     try:
#         num1 = int(input('Digite o primeiro numero: '))
#         num2 = int(input('Digite o segundo numero: '))
#     except:
#         print('Digite apenas números inteiros e não letras.')
#     else:
#         soma = num1+num2
#         print(f'O resultado da soma é {soma}.')
#         break

'''
10.8 - Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo menos três nomes de gatos no primeiro arquivo e três nomes
de cachorro no segundo arquivo. Escreva um programa que tente ler esses arquivos e mostre o conteudo do arquivo na tela. Coloque seu código
em um bloco try-except para capturar o erro FileNotFound e apresente uma mensagem simpatica caso o arquivo nao esteja presente. Mova um dos 
arquivos para um local diferente de seu sistema e garante que o codigo no bloco except seja executado de forma apropriada.'''
print('\nGatos e cachorros')
def ler_texto(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(f'O conteudo do arquivo é:\n{contents}')
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' does not exist.'
        print(msg)

filename = 'Arquivo_Exceções\\cats.txt', 'Arquivo_Exceções\\dogs.txt'
for n in filename:
    ler_texto(n)

'''
10.9 - Gatos e cachorros silenciosos: Modifique o seu bloco except para falhar silenciosamente caso um dos arquivos esteja ausente.'''
print('\nGatos e cachorros')
def ler_texto(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(f'O conteudo do arquivo é:\n{contents}')
    except FileNotFoundError:
        pass

filename = 'Arquivo_Exceções\\cats.txt', 'Arquivo_Exceções\\dogs.txt'
for n in filename:
    ler_texto(n)
