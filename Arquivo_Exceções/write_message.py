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

