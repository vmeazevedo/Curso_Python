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

