#Alterando, acrescentando e removendo elementos
#Modificando elementos de uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Acrescentando elementos em uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#Add elementos a uma lista vazia
print()
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserindo elementos em uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removendo elementos de uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#Removendo um item com o método pop() e armazendo ele em uma variável
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')

#Removendo itens de qualquer posição em uma lista
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(0)
print('The last motorcycle I owned was a ' + last_owned.title() + '.')

#Removendo uma item de acordo com o valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

'''
3.4 - Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o jantar, quem você convidaria?
Crie uma lista que inclua pelo menos três pessoas que você gostataria de convidar para jantar. Em seguida, utilize
sua lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.'''
print('\n3.4 - Lista de convidados')
lista = ['armando', 'jose', 'steve']
print('Olá ' + lista[0].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[1].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[2].title() + ' gostaria de jantar hoje comigo?')

'''
3.5 - Alterando a lista de convidados: Você acabou de saber que um de seus convidados não poderá comparecer ao jantar,
portanto será necessário enviar um novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.'''
print('\n3.5 - Lista de convidados')
lista = ['armando', 'jose', 'steve']
print('Olá ' + lista[0].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[1].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[2].title() + ' gostaria de jantar hoje comigo?')

print('O ' + lista[2].title() + ' infelizmente não poderá comparecer.')

lista[2] = 'elon'
print(lista)
print('Olá ' + lista[0].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[1].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[2].title() + ' gostaria de jantar hoje comigo?')

'''
3.6 - Mais convidados: Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível.
Pense em mais três, convidados para o jantar.'''
print('\n3.6 - Lista de convidados')
lista = ['armando', 'jose', 'elon']
print('Encontrei uma mesa de jantar maior!')
lista.insert(0, 'maria')
lista.insert(2, 'pedro')
lista.append('roberto')
print(lista)
print('Olá ' + lista[0].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[1].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[2].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[3].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[4].title() + ' gostaria de jantar hoje comigo?')
print('Olá ' + lista[5].title() + ' gostaria de jantar hoje comigo?')

'''
3.7 - Reduzindo a lista de convidados: Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o
jantar e tem espaço para somente dois convidados.'''
print('\n3.7 - Lista de convidados')
lista = ['armando', 'jose', 'elon']
print('Encontrei uma mesa de jantar maior!')
lista.insert(0, 'maria')
lista.insert(2, 'pedro')
lista.append('roberto')
print(lista)
print('Infelizmente a mesa não vai chegar a tempo, vou poder convidar apenas duas pessoas.')
popped_lista = lista.pop()
print('Infelizmente não poderia te convidar para o jantar ' + popped_lista.title() + '.')
print(lista)
popped_lista = lista.pop()
print('Infelizmente não poderia te convidar para o jantar ' + popped_lista.title() + '.')
print(lista)
popped_lista = lista.pop()
print('Infelizmente não poderia te convidar para o jantar ' + popped_lista.title() + '.')
print(lista)
popped_lista = lista.pop()
print('Infelizmente não poderia te convidar para o jantar ' + popped_lista.title() + '.')
print(lista)
del lista[0:2]
print(lista)

