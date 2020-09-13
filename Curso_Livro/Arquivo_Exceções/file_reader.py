import os

#Importando um arquivo utilizando 'os'
with open(os.path.join(os.path.dirname(__file__), 'pi_digits.txt')) as file_object:       
    contents = file_object.read()               #lemos o seu conteúdo com o método read() que coloca todo o conteúdo do arquivo em uma string única.
    print(contents.rstrip())

#Importando um arquivo por diretorio absoluto
print()
with open('C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

file_path = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#Lendo dados linha a linha
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#Criando uma lista de linhas de um arquivo
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()                 #O metodo readlines armazena cada linha do arquivo em uma lista.

for line in lines:
    print(line.rstrip())
