'''
9.10 - Importando Restaurant: Usando sua classe Restaurant mais recente armazene-a em um módulo. Crie um arquivo
separado que importe Restaurant. Crie uma instância de Restaurant e chame um de seus métodos para msotrar que a instrução
import funciona de forma apropriada.'''
from restaurant import Restaurant

restaunt = Restaurant('Ragazzo', 'organizada')
restaunt.describe_restaurant()
restaunt.open_restaurant()

'''
9.11 - Importando Admin: Comece com seu programa do ex 9.8. Armazene as classes User, Privileges e Admin em um módulo. Crie
um arquivo separado e uma instância da classe Admin e chame show_privileges() para mostrar que tudo está funcionando de forma apropriada.'''
from admin import User, Admin, Privileges

#Apresenta info de privilégios
priv = Admin('vinicius', 'azevedo', 28, 'mauá')
priv.privilegios.show_privileges()

'''
9.12 - Vários módulos: Armazene a classe User em um módulo e as classes Privileges e Admin em um módulo separado.
Em outro arquivo, crie uma instância de Admin e chame show_privileges() para mostrar que tudo continua funcionando de forma apropriada.'''
from admin import User
from admin import Admin             #No lugar de admin seria outro arquivo
from admin import Privileges        #No lugar de admin seria outro arquivo

#Apresenta info de privilégios
priv = Admin('vinicius', 'azevedo', 28, 'mauá')
priv.privilegios.show_privileges()