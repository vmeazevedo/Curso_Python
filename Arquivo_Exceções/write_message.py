#Escrevendo dados em um arquivo
#Escrevendo dados em um arquivo vazio

# r - modo de leitura
# w - modo de escrita
# a - modo de concatenação
# r+ - modo de leitura e escrita

filename = "C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\programming.txt"
with open(filename, 'w') as file_object:
    file_object.write('I love programming.')            #A função write cria um arquivo casos ele não existe, porém, caso ele já exista ela irá substitiuir o existente

#Escrevendo em arquivo ser especificar o diretorio absoluto.
filename = "Arquivo_Exceções\\programming2.txt"         #Para definir diretório sem ser absoluto é so colocar uma pasta do diretorio atual separado por duas \\
with open(filename, 'w') as file_object:
    file_object.write('I love programming2.')  

#Escrevendo várias linhas
filename =  "Arquivo_Exceções\\programming.txt"
with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
    file_object.write('I love creating new games.')     #A função write não acrescenta nenhuma quebra de linha ao texto

filename = 'Arquivo_Exceções\\programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')          #Add a quebra de linha para formatar melhor o nosso código
    file_object.write('I love creating new games.\n')

#======================================================

#Concatenando dados em um arquivo.
'''Criamos um arquivo com os dois valores iniciais.'''
filename = 'Arquivo_Exceções\\programming_concat.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')       
    file_object.write('I love creating new games.\n')
'''Depois acessamos o arquivo para add essas duas frases com a função de concatenar.'''
with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets. \n')
    file_object.write('I love creating apps that can run in a browser. \n')

'''
10.3 - Convidado: Escreva um programa que pergunte o nome ao usuário. Quando ele responder, escreva o nome em um
arquivo guest.txt.'''
# print('\n10.3 - Convidado')
# nome = input('Por gentileza, qual o seu nome? ')
# filename = 'Arquivo_Exceções\\guest.txt'
# with open(filename,'w') as file_object:
#     file_object.write(nome.title()+'.\n')

'''
10.4 - Lista de convidados: Escreva um laço while que pergunte o nome aos usuários. Quando fornecerem seus nomes,
apresente uma saudação na tela e acrescente uma linha que registre a visita do usuário em um arquivo chamado guest_book.txt.
Certifique-se de que cada entrada esteja em uma nova linha do arquivo.
'''
# print('\n10.4 - Lista de convidados')
# filename = 'Arquivo_Exceções\\guest_list.txt'
# while True:
#     nome = input('Por favor diga o seu nome: ')
#     with open(filename, 'a') as file_object:
#         file_object.write(nome.title() + '.\n')
#         print('Olá ' + nome.title() + '.')
#     escolha = input('Temos um novo registro? [S/N]: ')
#     if escolha == 's':
#         continue
#     else:
#         break

'''
10.5 - Enquete sobre programação: Escreva um laço while que pergunte as pessoas por que elas gostam de programação.
Sempre que alguém fornecer um motivo, acrescente-o em um arquivo que armazene todas as respostas.
'''
# print('\n10.5 - Enquete sobre programação')
# filename = 'Arquivo_Exceções\\enquete.txt'
# while True:
#     enquete = input('Por que você gosta de programação? ')
#     with open(filename,'a') as file_object:
#         file_object.write(enquete.capitalize() + '.\n')
#     escolha = input('Temos um novo registro? [S/N]: ')
#     if escolha == 's':
#         continue
#     else:
#         break


filename = 'Arquivo_Exceções\\enquete_2.txt'
while True:
    nome = input('Por favor, informe seu nome: ')
    filler = ': '
    enquete = input('Por que você gosta de programação? ')
    with open(filename,'a') as file_object:
        file_object.write(nome.title())
        file_object.write(filler)
        file_object.write(enquete.capitalize() + '.\n')
    escolha = input('Temos um novo registro? [S/N]: ')
    if escolha == 's':
        continue
    else:
        break
