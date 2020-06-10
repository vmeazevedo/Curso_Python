#Importando várias classes de um módulo
from car import Car, ElectricCar

my_beetle = Car('volkswagem', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


print()
#Importando um módulo completo
import car 

my_beetle = car.Car('volkswagem', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

