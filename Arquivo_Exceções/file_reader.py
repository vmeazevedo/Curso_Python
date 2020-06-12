import os

#Importando um arquivo utilizando 'os'
with open(os.path.join(os.path.dirname(__file__), 'pi_digits.txt')) as file_object:       
    contents = file_object.read()
    print(contents.rstrip())

#Importando um arquivo por diretorio absoluto
# with open('C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)