'''
11.1 - Cidade, país: Escreva uma função que aceite dois parâmetros: o nome de uma cidade e o nome de um país.
A função deve devolver uma única string no formato Cidade, País, por exemplo, Santiago, Chile. Armazene a função
em um módulo chamado city_functions.py

Crie um arquivo de nome test_cities.py que teste essa função que você acabou de escrever (lembre-se de que é 
necessário importar unittest e a função que você quer testar). Escreva um método chamado test_city_country() para
conferir se a chamada a sua função com valores como 'santiago, chile' resulta na strin correta. Execute test_cities.py
e garanta que test_city_country() passe no teste.
'''
import unittest
from city_functions import dados_pais

class NamesTestCase(unittest.TestCase):                        #Criamos uma classe que conterá varios testes de unidades, essa classe deve herdar da classe unittest.TestCase
    '''Testes para 'city_function.py'.'''

    def test_city_country(self):
        info_pais = dados_pais('santiago','chile')
        self.assertEqual(info_pais, 'Santiago, Chile')