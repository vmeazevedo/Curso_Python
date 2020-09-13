class Dog():
    '''Uma tentativa simples de modelar um cachorro.'''

    def __init__(self, name, age):
        '''Inicializa os atributos name e age.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simula um cachorro sentando em resposta a um comando.'''
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        '''Simula um cachorro rolando em resposta a um comando.'''
        print(self.name.title() + ' rolled over!')

#Criando uma instância a partir de uma classe
print('\n- Criando uma instância a partir de uma classe:')
my_dog = Dog('willie',6)
print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years old.')

#Chamando métodos
print('\n- Chamando métodos:')
my_dog = Dog('willie',6)
my_dog.sit()
my_dog.roll_over()

#Criando várias instâncias
print('\n- Criando várias instâncias:')
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print('My dog name is ' + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old.')
my_dog.sit()

print('\nYour dog name is ' + your_dog.name.title() + '.')
print('Your dog is ' + str(your_dog.age) + ' years old.')
your_dog.sit()

