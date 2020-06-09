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

class ElectricCar(Car):
    '''Representa aspectos de um carro específicos de veículos elétricos.'''

    def __init__(self, make, model, year):
        '''Inicializa os atributos da classe-pai.'''
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())