#Tratando a exceção FIleNotFoundError
filename = 'Arquivo_Exceções\\alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)
