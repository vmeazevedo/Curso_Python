#Passando um número arbitrário de argumentos
def make_pizza(*toppings):                                  #* nos permite add varios argumentos na mesma função
    '''Exibe a lista de ingredientes pedidos.'''
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    '''Apresenta a pizza que estamos prestes a preparar.'''
    print('\nMaking a pizza with the following toppings: ')
    for n in toppings:
        print('- '+ n)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Misturando argumentos posicionais e arbitrários
def make_pizza(size,*toppings):
    '''Apresenta a pizza que estamos prestes a preparar.'''
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    for n in toppings:
        print('- ' + n)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Usando argumentos nomeados arbitrários
print()
def build_profile(first, last, **user_info):
    '''Constroi um dicionário contendo tudo que sabemos sobre um usuário.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field= 'physics')
print(user_profile)



'''
8.12 - Sanduíches: Escreva uma função que aceite uma lista de itens que uma pessoa quer em um
sanduiche. A função deve ter um parâmetro que agrupe tantos itens quantos forem fornecidos pela
chamada da função e deve apresentar um resumo de sanduíches pedido. Chame a função três vezes
usando um número diferente de argumentos a cada vez.'''
print('\n8.12 -Sanduíche:')
def make_sanduba(*items):
    print(items)
make_sanduba('presunto')
make_sanduba('presunto', 'queijo')
make_sanduba('presunto', 'queijo', 'pão')

'''
8.13 - Perfil de usuário: Comece com uma cópia do codigo pag 210. Crie um perfil seu chamado build_profile(),
usando seu primeiro nome e o sobrenome, além de três outros pares chave-valor que o descrevam.'''
print('\n8.13 - Perfil de usuário:')
def build_profile(first, last, **user_info):
    dicionario = {}
    dicionario['first_name'] = first
    dicionario['last_name'] = last
    for key, value in user_info.items():
        dicionario[key] = value
    return dicionario

user_profile = build_profile('vinicius', 'azevedo', city ='mauá', age = 28)
print(user_profile)

'''
8.14 - Carros: Escreva uma função que armazene informações sobre um carro em um dicionário. A função
sempre deve receber o nome de um fabricante e um modelo. Um número arbitrário de argumentos nomeados então
deve ser aceito. Chame a função com as informações necessárias e dois outros pares, nome-valor, por exemplo,
uma cor ou um opcional. Sua função deve ser apropriada para uma chamada como essa:'''
print('\n8.14 - Carros:')
def dados_carro(fabricante, modelo, **opcionais):
    dic = {}
    dic['fabricante'] = fabricante
    dic['modelo'] = modelo
    for key, value in opcionais.items():
        dic[key] = value
    return dic
infos_carros = dados_carro('subaru', 'outback', color = 'blue', tow_package = True)
print(infos_carros)

