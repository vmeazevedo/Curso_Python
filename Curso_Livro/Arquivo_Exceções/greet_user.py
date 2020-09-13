import json

filename = 'Arquivo_Exceções\\username.json' 

with open(filename) as file_object:                 #Acessamos o arquivo em modo read
    username = json.load(file_object)               #Carregamos as informações e armazenamos na variavel username
    print('Welcome back, ' + username + '!')        #Apresentamos uma msg com o username armazenado


'''
10.11 - Número favorito: Escreva um programa que pergunte qual é o numero favorito de um usuário. Use json.dump() para
armazenar esse numero em um arquivo. Escreva um programa separado que leia esse valor e apresente a mensagem 'Eu sei
qual é o seu número favorito! É _______'.
'''
import json
print('\n10.11 - Numero favorito')
filename = 'Arquivo_Exceções\\number.json'
with open(filename) as file_object:
    number = json.load(file_object)
    print('Eu sei qual é o seu número favorito! É '+number+ '.')