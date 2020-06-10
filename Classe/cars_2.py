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

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Definindo um valor default para um atributo
''' 
- Atribuimos uma valor padrão para o odômetro (self.odometer_reading = 0) a class Car():
- Definimos uma função que irá apresentar o valor do odômetro;
- Chamamos a função com my_new_car.read_odometer().
'''

#Modificando valores de atributos
print()
my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Modificando o valor de um atributo com um método
'''Criamos uma função para realizar o update do odômetro, (self.odometer_reading = mileage) em def update_odometer(self, mileage):'''
print()
my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#Incrementando o valor de um atributo com um método
'''Criamos uma função para incrementar o valor do odômetro, (self.odometer_reading += miles) o qual irá add valores ao valor atual.'''
print()
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


'''
9.4 - Pessoas atendidas: Comece com seu programa 9.1. Acrescente um atributo chamado number_served cujo valor default é 0.
Crie uma instância chamada restaurant a partir dessa classe. Apresente o número de clientes atendidos pelo restaurante e, 
em seguida, mude esse valor e exiba-o novamente. 

Adicione um método chamado set_number_served() que permita definir o número de clientes atendidos. Chame esse método com 
um novo número e mostre o valor novamente.

Acrescente um método chamado increment_number_served() que permita incrementar o número de clientes servidos. Chame esse 
método com qualquer número que você quiser e que represente quantos clientes foram atendidos, por exemplo, em um dia de funcionamento.
'''
print()
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print('O restaurante ' + self.restaurant_name.title() + ' tem uma cozinha ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print('O restaurante ' + self.restaurant_name.title() + ' está aberto!')

    def servidos(self):
        print('O número de pessoas servidas no restaurante agora é de ' + str(self.number_served) + ' pessoas.')

    def set_number_served(self, servidos):
        self.number_served = servidos

    def increment_number_served(self, incremento):
        self.number_served += incremento

restaunt = Restaurant('Ragazzo', 'organizada')
restaunt.describe_restaurant()

restaunt.servidos()                             #Criamos uma função que apresente o numero de pessoas

restaunt.number_served = 2                      #Alteramos o valor de pessoas manualmente na self
restaunt.servidos()                             #Apresentamos o valor de pessoas

restaunt.set_number_served(3)                   #Alteramos o valor de pessoas com uma função na classe
restaunt.servidos()                             #Apresentamos o valor de pessoas

restaunt.increment_number_served(5)             #Incrementamos o valor do incremento ao numero de pessoas servidas
restaunt.servidos()                             #Apresentamos o valor de pessoas

'''
9.5 - Tentativas de login: Acrescente um atributo chamado login_attempts a sua claser User ex.9.3. Escreva um método
chamado increment_login_attempts() que incremente o valor de login_attempts em 1. Escreva outro método chamado
reset_login_attempts() que reinicie o valor de login_attempts com 0.

Crie uma instância da classe User e chame increment_login_attempts() varias vezes. Exiba o valor de login_attempts
para garantir que ele foi incrementado de forma apropriada e, em seguida, chame reset_login_attempts(). Exiba
login_attempts novamente para garantir que seu valor foi reiniciado com 0.'''
print()
class User():

    def __init__(self, first_name, last_name, age, city, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = login_attempts

    def describe_user(self):
        print('\nNome: ' + self.first_name.title() + ' ' + self.last_name.title() + ', Cidade: ' + self.city.title() + ', Idade: ' + str(self.age) + '.')
        print('Tentativas de login: ' + str(self.login_attempts) + '.')

    def increment_login_attempts(self, incremento):
        self.login_attempts += incremento

    def reset_login_attempts(self, reset):
        self.login_attempts = reset

info = User('vinicius', 'azevedo', 28, 'mauá')
info.describe_user()                                    #Apresentando valores default

info.increment_login_attempts(1)                        #Incrementando 4 tentantivas de logins
info.increment_login_attempts(1)
info.increment_login_attempts(1)
info.increment_login_attempts(1)
info.describe_user()                                    #Apresentando valores atualizados

info.reset_login_attempts(0)                            #Resetando as tentativas de logins
info.describe_user()                                    #Apresentando os valores atualizados
