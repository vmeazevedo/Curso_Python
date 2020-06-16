import json

filename = 'Arquivo_Exceções\\username.json' 

with open(filename) as file_object:                 #Acessamos o arquivo em modo read
    username = json.load(file_object)               #Carregamos as informações e armazenamos na variavel username
    print('Welcome back, ' + username + '!')        #Apresentamos uma msg com o username armazenado

    