#Testes de unidade e casos de teste
#Um teste que passa
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):                        #Criamos uma classe que conterá varios testes de unidades, essa classe deve herdar da classe unittest.TestCase
    '''Testes para 'name_function.py'.'''

    def test_first_last_name(self):                            #Criamos um metodo para checar se os nomes tem somente o nome e o sobrenome.
        '''Nomes como 'Janis Joplin' funcionam?'''             
        formatted_name = get_formatted_name('janis','joplin')  #Chamamos a função que queremos testar e armazenamos ela em um valor de retorno.
        self.assertEqual(formatted_name, 'Janis Joplin')       #Compara o valor em formatted_name com a string 'Janis Joplin' e retorna o resultado.

unittest.main()                                                #Diz ao Python para executar os testes desse arquivo.


#Um teste que falha
