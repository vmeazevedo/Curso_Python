#Usando instruções if com listas
#Verificando itens especiais
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')
print('\nFinished making your pizza!')

print()
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f'Adding {requested_topping}.')
print('\nFinished making your pizza!')


#Verificando se uma lista não esta vazia
print()
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

#Usando várias listas
print()
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print('\nFinished making your pizza!')

'''
5.8 - Olá admin: Crie uma lista com cinco ou mais nomes de usuarios, incluindo o nome 'admin'. Suponha que você esteja
escrevendo um codigo que exibira uma saudação a cada usuario depois que eles fizerem login em um site.
Percorra a lista com um laço e mostre uma saudação para cada usuário.'''
# print()
# lista = ['vinicius', 'maria', 'bruna', 'roberto', 'carlos', 'admin']
# usuario = str(input('Qual o seu usuario? '))

# if usuario == 'admin':
#     print('Olá admin, gostaria de ver um relatorio de status?')
#     for n in lista[1:]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')

# if usuario == 'vinicius':
#     print(f'Olá {usuario}, obrigado por fazer login novamente.')
#     for n in lista[1:5]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')
#     if 'admin' in lista:
#         print('Olá admin, gostaria de ver um relatorio de status?')

# if usuario == 'maria':
#     print(f'Olá {usuario}, obrigado por fazer login novamente.')
#     for n in lista[0:1]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')
#     for n in lista[2:5]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')
#     if 'admin' in lista:
#         print('Olá admin, gostaria de ver um relatorio de status?')

# if usuario == 'bruna':
#     print(f'Olá {usuario}, obrigado por fazer login novamente.')
#     for n in lista[0:2]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')
#     for n in lista[3:5]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')
#     if 'admin' in lista:
#         print('Olá admin, gostaria de ver um relatorio de status?')

# if usuario == 'roberto':
#     print(f'Olá {usuario}, obrigado por fazer login novamente.')
#     for n in lista[0:3]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')
#     for n in lista[4:5]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')
#     if 'admin' in lista:
#         print('Olá admin, gostaria de ver um relatorio de status?')

# if usuario == 'carlos':
#     print(f'Olá {usuario}, obrigado por fazer login novamente.')
#     for n in lista[0:4]:
#         print(f'Olá {n}, obrigado por fazer login novamente.')
#     if 'admin' in lista:
#         print('Olá admin, gostaria de ver um relatorio de status?')

# '''
# 5.9 - Sem usuário: Acrescente um teste if para garantir que a lista de usuário não esteja vazia.'''
# print()
# lista = ['vinicius', 'maria', 'bruna', 'roberto', 'carlos', 'admin']
# del(lista[0:])
# print(lista)
# if lista == []:
#     print('Precisamos encontrar alguns usuários!')

# print()
# lista = ['vinicius', 'maria', 'bruna', 'roberto', 'carlos', 'admin']
# lista.clear()
# print(lista)
# if lista == []:
#     print('Precisamos encontrar alguns usuários!')

# print()
# lista = ['vinicius', 'maria', 'bruna', 'roberto', 'carlos', 'admin']
# for n in lista[0:7]:
#     lista.pop()
# print(lista)
# if lista == []:
#     print('Precisamos encontrar alguns usuários!')


'''
5.10 - Verificando nomes de usuários: Faça o seguinte para criar um programa que simule o modo como os sites garantem
que todos tenham um nome de usuário único.'''
current_users = ['vinicius', 'roberto', 'carlos', 'maria', 'bruna']
new_users = ['vinicius', 'ROBertO', 'carol', 'fernanda', 'marta']

for n in new_users:
    if n.lower() in current_users:
        print(f'O nome {n.title()} já foi utilizado, por favor utilize um outro nome.')
    if n.lower() not in current_users:
        print(f'O nome {n.title()} está disponivel.')

'''
5.11 - Números ordinais: Números ordinais indicam sua posição em uma lista, por exemplo, 1st ou 2sd em inglês.
A maioria dos numeros ordinais nessa lingua termina com th, exceto 1,2 e 3.'''
print()
num = [1,2,3,4,5,6,7,8,9]

for n in num:
    if n == 1:
        print(f'{n}st')
    elif n == 2:
        print(f'{n}nd')
    elif n == 3:
        print(f'{n}rd')
    else:
        print(f'{n}th')
    