print('\n9.8 - Privilégios')
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
        self.privilegios = Privileges(self)
        
class Privileges():
    def __init__(self, privileges):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Os privilégios desse usuário são:')
        for n in self.privileges:
            print(n.capitalize() + '.') 

#Apresenta infos de usuário
info = User('vinicius', 'azevedo', 28, 'mauá')
info.describe_user()
info.greet_user()
#Apresenta info de privilégios
priv = Admin('vinicius', 'azevedo', 28, 'mauá')
priv.privilegios.show_privileges()