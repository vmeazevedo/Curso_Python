class Car():
    '''Uma tentativa simples de representar um carro.'''

    def __init__(self, make, model, year):
        '''Inicializa os atributos que descrevem um carro.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Devolve um nome descritivo, formatado de modo elegante.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''Exibe uma frase que mostra a milhagem do carro.'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        '''Define o valor de leitura do odômetro com o valor especificado.
        Rejeita a alteração se for tentativa de definir um valor menor para o odômetro.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not go back a odometer!')

    def increment_odometer(self, miles):
        '''Soma a quantidade especifica ao valor de leitura do odômetro.'''
        self.odometer_reading += miles

#FILHA
class Battery():
    '''Uma tentativa simples de modelar uma bateria para um carro elétrico.'''

    def __init__(self, battery_size=70):
        '''Inicializa os atributos da bateria.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Exibe uma frase que descreve a capacidade da bateria.'''
        print('This car has a ' + str(self.battery_size) + '-kWh battery.') 

    def get_range(self):
        '''Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria.'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = 'This car can go approximately ' + str(range) + ' miles on full charge.'
        print(message)

class ElectricCar(Car):
    '''Representa aspectos de um carro específicos de veículos elétricos.'''

    def __init__(self, make, model, year):
        '''
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico.
        '''
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


'''
9.6 - Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma classe chamada IceCreamStand
 que herde da classe Restaurant escrita no ex 9.1. Adicione um atributo chamado flavors que armazene uma lista de sabores de sorvete.
 Escreva um método para mostrar esses sabores. Crie uma instância de IceCreamStand e chame esse método.'''
print('\n9.6 - Sorveteria')
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('O restaurante ' + self.restaurant_name.title() + ' tem uma cozinha ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('O restaurante ' + self.restaurant_name.title() + ' está aberto!')

class IceCreamStand(Restaurant):                                        #Classe que herda Restaurant criada
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['morango','chocolate','caramelo']               #Atributo flavors adicionado a classe filha
    
    def describe_flavors(self):                                         #Método escrito para demostrar os sabores disponíveis
        print('Os sabores disponíveis são: ')
        for n in self.flavors:
            print(n.title() + '.')
        
restaunt = Restaurant('Ragazzo', 'organizada')
restaunt.describe_restaurant()
restaunt.open_restaurant()

sorvete = IceCreamStand('Ragazzo', 'organizada')                        #Instância de IceCreamStand criada
sorvete.describe_flavors()                                              #Chamando o método com as informações de sabores.


'''
9.7 - Admin: Um administrador é um tipo especial de usuário. Escreva uma classe chamada Admin
 que herde da classe User escrita no ex 9.3. Adicione um atributo privileges que armazene uma lista de strings como 
 'can add post', 'can delete post', 'can ban user', e assim por diante. Escreva uma método chamado show_privileges()
 que liste o conjunto de privilégios de um adiministrador. Crie uma instância de admin e chame seu método.'''
print('\n9.7- Admin')
class User():
    def __init__(self, first_name, last_name, age, city='santo andre'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def describe_user(self):
        print('\nNome: ' + self.first_name.title() + ' ' + self.last_name.title() + ', Cidade: ' + self.city.title() + ', Idade: ' + str(self.age) + '.')

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print('Olá ' + full_name.title() + ', seja bem vindo ao Itaú!' )


class Admin(User):
    def __init__(self, first_name, last_name, age, city='santo andre'):
        super().__init__(first_name, last_name, age, city=city)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Os privilégios desse usuário são:')
        for n in self.privileges:
            print(n.capitalize() + '.')   

info = User('vinicius', 'azevedo', 28, 'mauá')
info.describe_user()
info.greet_user()

priv = Admin('vinicius', 'azevedo', 28, 'mauá')
priv.show_privileges()