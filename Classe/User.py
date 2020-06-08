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

info = User('vinicius', 'azevedo', 28, 'mauá')
info.describe_user()
info.greet_user()

info = User('carlos', 'gomes', 60, 'mauá')
info.describe_user()
info.greet_user()

info = User('iolanda', 'mendes', 54,)
info.describe_user()
info.greet_user()
