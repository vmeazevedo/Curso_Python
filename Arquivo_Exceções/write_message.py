#Escrevendo dados em um arquivo
#Escrevendo dados em um arquivo vazio

# r - modo de leitura
# w - modo de escrita
# a - modo de concatenação
# r+ - modo de leitura e escrita

filename = "C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\programming.txt"

with open(filename, 'w') as file_object:
    file_object.write('I love programming.')

