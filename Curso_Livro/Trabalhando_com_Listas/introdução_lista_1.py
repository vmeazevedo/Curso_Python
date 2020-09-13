#Acessando elementos em uma lista
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

#A posição do indice começa em 0 e não em 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

#Devolvendo o ultimo indice
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

#Usando valores individuais de uma lista
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)

'''
Experimente criar estes programas pequenos para ter um pouco de experiência própria com listas em Python.
Você pode criar uma nova pasta para os exercícios de cada capítulo a fim de mantê-los organizados.

3.1 - Nomes: Armazene os nomes de alguns de seus amigos em uma lista chamada names. Exiba o nome de cada pessoa
acessando cada elemento da lista, um de cada vez.'''
print('\n3.1 - Nomes')
amigos = ['eduardo', 'julião', 'sommerhauzer']
print(amigos[0].title())
print(amigos[1].title())
print(amigos[2].title())

'''
3.2 - Saudações: Comece com a lista usada no 3.1, mas em vez de simplesmente exibir o nome de cada pessoa,
apresente uma mensagem a elas. O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve estar
personalizada com o nome da pessoas.'''
print('\n3.2 - Saudações')
amigos = ['eduardo', 'julião', 'sommerhauzer']
print('O ' + amigos[0].title() + ' é meu amigo.')
print('O ' + amigos[1].title() + ' é meu amigo.')
print('O ' + amigos[2].title() + ' é meu amigo.')

'''
3.3 - Sua própria lista: Pense em seu meio de transporte preferido, como motocicleta ou carro, e crie uma
lista que armazene vários exemplos. Utilize sua lista para exibir uma série de frases sobre esses itens, como
"Gostaria de ter uma moto Honda".'''
print('\n3.3 - Sua própria lista')
motos = ['bmw', 'honda', 'yamaha', 'suzuki']
print('As motos da ' + motos[0].upper() + ' são muito grandes.')
print('A ' + motos[1].title() + ' faz motos muito boas.')
print('A Midnight é o modelo da ' + motos[2].title() + ' que eu mais gosto.')
print('A ' + motos[3].title() + ' Intruder, é pau pra toda obra!')