import json
'''
Carrega o nome do usuário se oi armazenado anteriormente
Caso contrário, pede que o usuário forneça o nome e armazena essa informação
'''
#Add registros dentro de um arquivo com json
# username = input('What is your name? ')
# filename = 'Arquivo_Exceções\\username.json'                           
# with open(filename,'w') as file_object:
#     json.dump(username, file_object)

# #Add e lendo registros json com bloco try-except
# filename = 'Arquivo_Exceções\\username.json'                           
# try:
#     with open(filename) as file_object:
#         username = json.load(file_object)                                    
# except FileNotFoundError:
#     username = input('What is your name? ')                                 
#     with open(filename,'w') as file_object:                                 
#         json.dump(username, file_object)                                    
#         print('We will remember you when you come back, ' + username + '!')  
# else:
#     print('Welcome back, ' +username+ '!')

#Refatoraçao
def get_stored_username():
    '''Obtém o nome de usuário já armazenado se estiver disponível.'''
    filename = 'Arquivo_Exceções\\username.json'                           
    try:
        with open(filename) as file_object:
            username = json.load(file_object)                                    
    except FileNotFoundError:
        return None  
    else:
        return username

def get_new_username():
    '''Pede um novo nome de usuário.'''
    username = input('What is your name? ')                                 
    filename = 'Arquivo_Exceções\\username.json'
    with open(filename,'w') as file_object:
        json.dump(username, file_object)
    return username    

def greet_user():
    '''Saúda o usuário pelo nome.'''
    username = get_stored_username()
    if username:
        print('Welcome back, ' +username+ '!')
    else:
        username = get_new_username()
        print('We will remember you when you come back, ' + username + '!')  

greet_user()


'''
10.11 - Número favorito: Escreva um programa que pergunte qual é o numero favorito de um usuário. Use json.dump() para
armazenar esse numero em um arquivo. Escreva um programa separado que leia esse valor e apresente a mensagem 'Eu sei
qual é o seu número favorito! É _______'.'''
# print('\n10.11 - Numero favorito')
# import json
# number = input('Qual o seu numero favorito? ')
# filename = 'Arquivo_Exceções\\number.json'                           
# with open(filename,'w') as file_object:
#     json.dump(number, file_object)

'''
10.12 - Lembrando o número favorito: Combine os dois programas do Exercicio anterior em um unico arquivo. Se o numero já estiver
armazenado, informe o número favorito ao usuário. Caso contrário, pergunte ao usuário qual é o seu numero favorito e armazene-o
em um arquivo. Execute o programa duas vezes para garantir que ele funciona.
'''
print('\n10.12 - Lembrando o numero favorito')
import json
filename = 'Arquivo_Exceções\\number.json'                           
try:
    with open(filename) as file_object:
        number = json.load(file_object)                                    
except FileNotFoundError:
    number = input('Qual o seu numero favorito? ')                                 
    with open(filename,'w') as file_object:                                 
        json.dump(number, file_object)                                    
        print('Agora irei sempre me lembra que seu numero favorito é, ' + number + '!')  
else:
    print('Eu sei qual é o seu número favorito! É, ' +number+ '!')



