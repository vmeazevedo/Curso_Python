'''
10.1 - Aprendendo Python: Abra um arquivo em branco em seu editor de texto e escreva algumas linhas que
sintetizem o que você aprendeu sobre Python até agora. Comece cada linha com a expressão Em Python podemos...
Salve o arquivo como learning_python.txt no mesmo diretório em que estão seus exercícios deste capítulo.
Escreva um programa que leia o arquivo e mostre o que você escreveu, três vezes. Exiba o conteúdo uma vez
lendo o arquivo todo, uma vez percorrendo o objeto arquivo com um laço, e outra armazenando as linhas em uma lista
e então trabalhando com ela fora do bloco with.
'''
#Exiba o conteúdo uma vez lendo o arquivo todo
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\learning_python.txt'     #Identificamos o local do arquivo
with open(filename) as file_object:                                                                             #Abrimos o arquivo como objeto
    conteudo = file_object.read()                                                                               #Acessamos a variavel com o metodo read.
    print(conteudo)                                                                                             #Printamos o conteudo do arquivo    
    print()

#Uma vez percorrendo o objeto arquivo com um laço
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\learning_python.txt'     #Identificamos o local do arquivo
with open(filename) as file_object:                                                                             #Abrimos o arquivo como objeto                 
    for line in file_object:                                                                                    #Acessamos cada linha do conteudo do arquivo com um laço
        print(line.rstrip())                                                                                    #Printamos o conteúdo formatado
print()

#E outra armazenando as linhas em uma lista e então trabalhando com ela fora do bloco with
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\learning_python.txt'     #Identificamos o local do arquivo     
with open(filename) as file_object:                                                                             #Abrimos o arquivo como objeto
    lines = file_object.readlines()                                                                             #Acessamos a variável com o metodo readlines

for n in lines:                                                                                                 #Para cada item dentro da variável            
    print(n.rstrip())                                                                                           #Printamos o conteúdo formatado
