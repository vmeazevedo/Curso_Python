#Trabalhando com o conteúdo de um arquivo
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#Arquivos grandes: um milhão de dígitos
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

#Seu aniversário está contido em pi?
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the firs million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi.')