#Trabalhando com o conteúdo de um arquivo
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))