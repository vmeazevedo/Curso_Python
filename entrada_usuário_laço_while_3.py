#Usando um laço while com listas e dicionários
#Transferindo itens de uma lista para outra
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()          #Retira o ultimo nome da lista com o metodo pop() e guarda o valor na variavel
    print('Verify user: ' + current_user.title())   #Printa o valor salvo na variavel
    confirmed_users.append(current_user)            #Add o valor na lista confirmed_user com o metodo append()

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:              #Exibe cada item da nova lista com o laço for
    print(confirmed_user.title())

#Removendo todas as instâncias de valores especificos de uma lista
print()
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# #Preenchendo um dicionário com dados de entrada do usuário
# print()
# responses = {}
# polling_active = True
# while polling_active:
#     name = input('What is your name? ')
#     response = input('Which mountain would you like to climb someday? ')
    
#     responses[name] = response                                              #Armazena a resposta no dicionário / 'nome': 'resposta'

#     repeat = input('Would you like to let another person respond? [Y/N]: ') #Verifica se haverá outra resposta a ser computada.
#     if repeat == 'no':
#         polling_active = False

# print('\n--- Poll Results ---')
# for name, response in responses.items():                                    #Exibe a chave e o valor dentro do dicionario na frase.
#     print(name + ' would like to climb ' + response + '.')

'''
7.8 - Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com os nomes de vários sanduíches.
Em seguida, crie uma lista vazia chamada finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço
e mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduiche de atum. A medida que cada sanduiche
for preparado, transfira-o para a lista de sanduiches prontos. Depois que todos os sanduiches estiverem prontos
mostre uma mensagem que liste cada sanduiche preparado.'''
print('\n7.8 - Lanchonete')
sandwich_orders = ['atum', 'hamburguer', 'mortadela']
finished_sandwiches = []

while sandwich_orders:
    current_sand = sandwich_orders.pop()
    print('Preparei o seu sanduiche de ' + current_sand.title())
    finished_sandwiches.append(current_sand)
print('\nLista de sanduiches prontos:')
for n in finished_sandwiches:
    print(n.title())

'''
7.9 - Sem pastrami: Usando a lista sandwich_ordes, garanta que o sanduiche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código proximo ao inicio de seu programa para exibir uma mensagem informando que a lanchonete está sem pastrami e,
então, use um laço while para remover todas as ocorrências de 'pastrami' em sandwich_orders. Garanta que nenhum sanduiche de pastrami 
acabe em finished_sandwiches.'''

print('\n7.8 - Sem pastrami')
sandwich_orders = ['atum', 'hamburguer', 'mortadela', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []
print('Atenção: A lanchonete está sem pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sand = sandwich_orders.pop()
    print('Preparei o seu sanduiche de ' + current_sand.title())
    finished_sandwiches.append(current_sand)
print('\nLista de sanduiches prontos:')
for n in finished_sandwiches:
    print(n.title())

'''
7.10 - Férias dos sonhos: Escreva um programa que faça uma enquete sobre as férias dos sonhos dos usuários. Escreva um prompt semelhante a este:
Se pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que apresente os resultados da enquete.'''
print('\n7.10 - Férias dos sonhos')
print('Se pudesse visitar um lugar do mundo, para onde você iria?')
lista = []

while True:
    resp = input('Digite aqui a sua resposta: ')
    lista.append(resp.title())
    repeat = input('Gostaria de dizer algum outro lugar? [S/N]: ')
    if repeat == 'n':
        break
print('\nO resultado da enquete dos lugares que você gostaria de visitar foi:')
for n in lista:
    print(n)